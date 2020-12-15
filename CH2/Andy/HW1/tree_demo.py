# demo of tree structures


class TreeNode:
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node: {0.val}; Left Leave: {0.left.val}; Right Leave: {0.right.val}'.format(
            self)


tr1 = TreeNode('A')
tr2 = TreeNode('B')
tr3 = TreeNode('C')
tr4 = TreeNode('D')
tr5 = TreeNode('E')
tr6 = TreeNode('F')
tr7 = TreeNode('G')

tr1.left = tr2
tr1.right = tr3

tr2.left = tr4
tr2.right = tr5

tr3.left = tr6
tr3.right = tr7

#       A
#      / \
#     B   C
#    / \ / \
#   D  EF   G


def DFS(tr):  # depth-first Search
    if tr is None:
        return
    print(tr.val)
    DFS(tr.left)
    DFS(tr.right)


DFS(tr1)
'''
>>> A
    B
    D
    E
    C
    F
    G
'''
