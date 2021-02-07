# Binary Tree class
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
      """Build binary tree through node.
      The first travel builds nodes.
      The second travel initialize value of root and children
      """
      node_dict = {}
      for node_data in node_list:
          data = node_data['data']
          node_dict[data] = BinTreeNode(data)
      for node_data in node_list:
          data = node_data['data']
          node = node_dict[data]
          if node_data['is_root']:
              root = node
          node.left = node_dict.get(node_data['left'])
          node.right = node_dict.get(node_data['right'])
      return cls(root)

    # Preorder travel binary tree by using recursive way
    def recursive_preordertravel(self, subtree):
        """Process the root of tree(subtree)
        Then left child and then right child."""
        if subtree is not None:
            print(subtree.data)
            self.recursive_preordertravel(subtree.left)
            self.recursive_preordertravel(subtree.right)


    def recursive_inordertravel(self, subtree):
        if subtree is not None:
            self.recursive_inordertravel(subtree.left)
            print(subtree.data)
            self.recursive_inordertravel(subtree.right)


    def recursive_postordertravel(self, subtree):
        if subtree is not None:
            self.recursive_postordertravel(subtree.left)
            self.recursive_postordertravel(subtree.right)
            print(subtree.data)


if __name__ == '__main__':
    node_list = [
        {'data' : 'A', 'left' : 'B', 'right' : 'C', 'is_root' : True},
        {'data' : 'B', 'left' : 'D', 'right' : 'E', 'is_root' : False},
        {'data' : 'D', 'left' : None, 'right' : None, 'is_root' : False},
        {'data' : 'E', 'left' : 'H', 'right' : None, 'is_root' : False},
        {'data' : 'H', 'left' : None, 'right' : None, 'is_root' : False},
        {'data' : 'C', 'left' : 'F', 'right' : 'G', 'is_root' : False},
        {'data' : 'F', 'left' : None, 'right' : None, 'is_root' : False},
        {'data' : 'G', 'left' : 'I', 'right' : 'J', 'is_root' : False},
        {'data' : 'I', 'left' : None, 'right' : None, 'is_root' : False},
        {'data' : 'J', 'left' : None, 'right' : None, 'is_root' : False},
    ]

    btree=BinTree.build_from(node_list)
    btree.recursive_preordertravel(btree.root)
    btree.recursive_inordertravel(btree.root)
    btree.recursive_postordertravel(btree.root)
