from tree_sisters.tree_annotator import TreeAnnotator
from nose.tools import assert_equals, assert_true
from skbio.tree import TreeNode
from StringIO import StringIO
import IPython

class TestTree2TaxNamedClusters:
    def testFindParents(self):
        ann = TreeAnnotator()
        
        tree = TreeNode.read(StringIO("(((A:1, B:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('B', ann.find_parent_name(tree, tree.find('B')), 'parent is self')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('g__genus1', ann.find_parent_name(tree, tree.find('2475')), 'parent directly above')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        assert_equals('f__family', ann.find_parent_name(tree, tree.find('2475')), 'parent 2 above')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6)'f__family':10);"))
        assert_equals(None, ann.find_parent_name(tree, tree.find('f__family').parent), 'parent of root')
        
        tree = TreeNode.read(StringIO("(((A:1, 2475:2):3, (C:4, D:5)'g__genus2':6):10);"))
        assert_equals(None, ann.find_parent_name(tree, tree.find('g__genus2').parent), 'no parent before root')
        
    def testSistersSelf(self):
        ann = TreeAnnotator()
        tree = TreeNode.read(StringIO("(((A:1, B:2)'g__genus1':3, (C:4, D:5)'g__genus2':6)'f__family':10)root;"))
        sisters = ann.find_sisters(tree, tree.find('B'))
        assert_equals(['B'], [s.name for s in sisters])
        