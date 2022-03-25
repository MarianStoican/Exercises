import sys
import pytest
from exercises.serialize_function import encode, decode, BinaryTree, BinaryTreeNode


class TestEncoderDecoder:

    def setup_method(self):
        def create_binary_tree():
            tree = BinaryTree(root=1)
            tree.populate([2, 3, 5, 6, None, 7])
            return tree
        self.tree = create_binary_tree()

    def test_encode_decode(self):
        encoded_string = encode(self.tree)
        resulted_tree = decode(encoded_string)

        assert self.tree.compare_trees(resulted_tree.root)
        assert resulted_tree.compare_trees(decode(encode(resulted_tree)).root)

    @staticmethod
    def test_wrong_input_data():
        data1 = [1232, BinaryTreeNode(2)]
        for data in data1:
            with pytest.raises(Exception) as e:
                encode(data)
            assert e.value.args[0] == 'The data must be a BinaryTree!'

        data2 = [12]
        with pytest.raises(Exception) as e:
            decode(data2)
        assert e.value.args[0] == 'The data must be string!'

    def test_different_separator(self):
        encoded_tree = encode(self.tree)
        separator = ';'
        with pytest.raises(Exception) as e:
            decode(encoded_tree, separator)
        assert e.value.args[0] == 'For encode it was used different separator!'


if __name__ == "__main__":
    pytest.main(sys.argv)
