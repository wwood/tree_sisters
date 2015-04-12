#!/usr/bin/env python2.7

import logging
from skbio.tree import TreeNode
import os
import sys
import argparse
import tree2tax

try:
    import tree_sisters.tree_annotator
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..'))
from tree_sisters.tree_annotator import TreeAnnotator

parser = argparse.ArgumentParser(description='''--- tree_sisters %s --- annotate leaves on a phylogenetic tree by printing out parent and sister clades''' % tree2tax.__version__)
parser.add_argument('-t', '--tree', help='annotated newick format tree file', required=True)
parser.add_argument('--debug', help='output debug information', action="store_true")

args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# read in Tree
logging.info("Reading in tree file %s" % args.tree)
tree = TreeNode.read(args.tree)
logging.info("Read in tree with %i leaves" % len(tree.tips()))

# read in list of leaves to be annotated (not yet implemented)
leaves_to_annotate = tree.tips() #an iterator

# for each Leaf
annotator = TreeAnnotator()
count = 0
for leaf in leaves_to_annotate:
    # determine its parent by ascending the tree until an annotated node or the root is reached
    parent = annotator.find_parent_name(tree, leaf)
    parent_name = ''
    if parent:
        parent_name = parent.name
    
    sisters = annotator.find_sister(tree, leaf)
    print "\t".join([leaf.name,
                     parent_name,
                     ",".join([s.name for s in sisters])])
    count += 1

logging.info("Printed info %i leaves" % count)
