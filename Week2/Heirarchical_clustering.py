__author__ = 'Siddhant'

import sys


def interpreter(conn):
    nn = int(conn.readline().strip())
    dd = dict()
    for i, lin in enumerate(conn):
        for j, value in enumerate(lin.strip().split(' ')):
            if i != j:
                dd[(i, j)] = float(value)
    return nn, dd


class Node(object):
    def __init__(self, index, leaf, left=None, right=None, age=0):
        self.index = index
        self.leaf = leaf
        if leaf:
            self.age = 0
            self.elements = 1
        if not leaf:
            self.left = left
            self.right = right
            self.age = age
            self.elements = left.elements+right.elements


def initialize(nn):
    t = list()
    for i in range(nn):
        t.append(Node(i, True))
    return t


def reduce_tree():
    global tree, int_node, d, l
    a, b = min(d, key=d.get)
    for node in tree:
        if node.index == a:
            node_a = node
        elif node.index == b:
            node_b = node
    l = list()
    node_printer(node_a)
    node_printer(node_b)
    g.write(' '.join(l)+'\n')
    tree.remove(node_a)
    tree.remove(node_b)
    new_node = Node(int_node, False, node_a, node_b, d[a, b]/2)
    tree.append(new_node)
    el_a = node_a.elements
    el_b = node_b.elements
    for node in tree:
        ind = node.index
        if ind != int_node:
            d[int_node, ind] = (d[a, ind]*el_a + d[b, ind]*el_b)/(el_a+el_b)
            d[ind, int_node] = (d[a, ind]*el_a + d[b, ind]*el_b)/(el_a+el_b)
    for key, value in list(d.items()):
        i, j = key
        if i == a or i == b or j == a or j == b:
            del d[key]
    int_node += 1
    return None


def node_printer(nodal):
    global l
    if nodal.leaf:
        l.append(str(nodal.index+1))
    else:
        node_printer(nodal.left)
        node_printer(nodal.right)
    return None

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        n, d = interpreter(f)
    int_node = n
    tree = initialize(n)
    g = open('hierarch_out.txt', 'w')
    while len(tree) > 1:
        reduce_tree()
    g.close()