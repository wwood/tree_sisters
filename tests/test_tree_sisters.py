from tree_sisters.tree_annotator import TreeAnnotator
from nose.tools import assert_equals, assert_true
from skbio.tree import TreeNode
from StringIO import StringIO

class TestTree2TaxNamedClusters:
    def testFindParents(self):
        ann = TreeAnnotator()
        
        tree = TreeNode.read(StringIO("(((A:1, B:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('g__genus1', ann.find_named_parent(tree, tree.find('B')).name, 'self is named')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('g__genus1', ann.find_named_parent(tree, tree.find('2475')).name, 'parent directly above')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('f__family', ann.find_named_parent(tree, tree.find('2475')).name, 'parent 2 above')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6)'f__family':10);"))
        assert_equals(None, ann.find_named_parent(tree, tree.find('f__family').parent), 'parent of root')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6):10);"))
        assert_equals(None, ann.find_named_parent(tree, tree.find('g__genus2').parent), 'no parent before root')
        
              
    def testSistersHelloWorld(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("(((A:1, B:2):3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals(['g__genus2'], [s.name for s in sisters])   
        
    def testSistersSelfNoParent(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("(((A:1, B:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals([], [s.name for s in sisters])  

    def testSistersTwoSistersEqualLevel(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("((A:1, B:2):3, ((C:1,D:1)'g2':1, (E:1,F:5)'g3':6):10)root;"))
        print(tree.ascii_art())
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals(sorted(['g2','g3']), sorted([s.name for s in sisters]))

    def testSistersOneIncompleteSister(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("((A:1, B:2):3, ((C:1,D:1):1, (E:1,F:5)'g3':6):10)root;"))
        print(tree.ascii_art())
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals(sorted(['g3']), sorted([s.name for s in sisters]))
        
    def testSistersSisterWithDescendentNames(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("((A:1, B:2):3, (((a:1,b:1)'s1':1,D:1)'g2':1, (E:1,F:5)'g3':6):10)root;"))
        print(tree.ascii_art())
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals(sorted(['g2','g3']), sorted([s.name for s in sisters]))
        
    def testFullTaxonomy(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("(((A:1, B:2):3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('f__family; g__genus2', ann.full_taxonomy(tree, tree.find('D')))

        
