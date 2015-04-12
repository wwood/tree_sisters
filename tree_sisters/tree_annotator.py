from tree2tax.tree2tax import TaxonomyFunctions

class TreeAnnotator:
    def find_parent_name(self, tree, node):
        n = node
        while (n is not None):
            name = TaxonomyFunctions().taxonomy_from_node_name(n.name)
            if (name is not None):
                return name
            else:
                n = n.parent
        return None
    
    def find_sisters(self, tree, node):
        '''return a list of nodes that are named sister lineage LCAs (may be 0, 1 or more nodes that fit this description)'''
        
        stack = Stack() # collection of nodes that may contain sister lineages
        sisters = []
        n = node
        while len(sisters) == 0 and n is not None:
            while n is not None:
                name = TaxonomyFunctions().taxonomy_from_node_name(n.name)
                if name is not None:
                    # this node is a sister
                    sisters.append(n)
                else:
                    # not named, descend further
                    for d in n.children:
                        stack.push(d)

            if len(sisters) == 0:
                # no sisters found at this level, go up one and try again
                n = n.parent
            
class Stack:
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return len(self.__storage) == 0

    def push(self,p):
        self.__storage.append(p)

    def pop(self):
        return self.__storage.pop()