import sys
import pytest
from exercises.next_alphabetical_permutation import next_alphabetical_permutation


def test_next_alphabetical_permutation():
    data1 = ['c', 'b', 'a']
    permuted_data1 = ['a', 'b', 'c']
    data2 = ['c', 'a', 'b']
    permuted_data2 = ['c', 'b', 'a']
    data3 = ['a', 'c', 'b']
    permuted_data3 = ['b', 'a', 'c']
    data4 = ['b', 'c', 'a']
    permuted_data4 = ['c', 'a', 'b']
    data5 = ['A', 'd', 'c', 'a']
    permuted_data5 = ['a', 'A', 'c', 'd']

    assert next_alphabetical_permutation(data1) == permuted_data1
    assert next_alphabetical_permutation(data2) == permuted_data2
    assert next_alphabetical_permutation(data3) == permuted_data3
    assert next_alphabetical_permutation(data4) == permuted_data4
    assert next_alphabetical_permutation(data5) == permuted_data5


def test_wrong_input_data():
    data1 = ['a', 'v', 12, 'd']
    data2 = ['[', '{', '.', '/']

    for data in [data1, data2]:
        assert next_alphabetical_permutation(data) == 'The input must be a sequence of' \
                                                      ' alphabetical chars'


if __name__ == "__main__":
    pytest.main(sys.argv)
