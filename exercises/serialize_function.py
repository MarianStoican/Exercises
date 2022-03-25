class BinaryTreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left_child = None
        self.__right_child = None

    @property
    def data(self):
        return self.__data

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, value):
        self.__left_child = value

    @property
    def right_child(self):
        return self.__right_child

    @right_child.setter
    def right_child(self, value):
        self.__right_child = value


class BinaryTree:
    def __init__(self, root):
        if isinstance(root, BinaryTreeNode):
            self.__root = root
        else:
            self.__root = BinaryTreeNode(root)

    @property
    def root(self):
        return self.__root

    def populate(self, values):
        if not values:
            return None
        it = iter(values)
        q = [self.__root]
        for node in q:
            val = next(it, None)
            if val:
                node.left_child = BinaryTreeNode(val)
                q.append(node.left_child)
            val = next(it, None)
            if val:
                node.right_child = BinaryTreeNode(val)
                q.append(node.right_child)

    def compare_trees(self, root):
        def are_binary_trees_identical(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2:
                return ((node1.data == node2.data) and
                        are_binary_trees_identical(node1.left_child,
                                                   node2.left_child) and
                        are_binary_trees_identical(node1.right_child,
                                                   node2.right_child))
            return False

        return are_binary_trees_identical(self.__root, root)


def encode(tree, separator=','):
    def dfs(node):
        nonlocal encoded
        if not node:
            encoded += ('\0' + separator)
        else:
            encoded += (str(node.data) + separator)
            dfs(node.left_child)
            dfs(node.right_child)

    encoded = ''
    if not isinstance(tree, BinaryTree):
        raise Exception('The data must be a BinaryTree!')
    dfs(tree.root)
    encoded += separator
    return encoded


def decode(data, separator=','):
    def dfs():
        nonlocal index
        if index == len(decoded):
            return None
        if decoded[index] == '\0':
            index += 1
            return None
        node = BinaryTreeNode(int(decoded[index]))
        index += 1
        node.left_child = dfs()
        node.right_child = dfs()
        return node

    if not isinstance(data, str):
        raise Exception('The data must be string!')
    old_separator = data[-1]
    data.rstrip(old_separator)
    if old_separator != separator:
        raise Exception('For encode it was used different separator!')
    decoded = data.split(separator)
    index = 0
    tree = BinaryTree(dfs())
    return tree
