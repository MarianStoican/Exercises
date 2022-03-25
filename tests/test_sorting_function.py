import sys
import pytest
from random import randint
from exercises.sorting_function import sorting_array_function

data1 = [2, 3, 4, 1]
sorted_data1 = [1, 2, 3, 4]

data2 = [randint(1, 30) for _ in range(0, 10000)]
sorted_data2 = data2[:]
sorted_data2.sort()

data3 = [1]

data4 = [1, 4, 2, 60, 0.3, 2, 4.3]


def test_sorting_array_function():
    result1 = sorting_array_function(data1)
    result2 = sorting_array_function(data2)
    result3 = sorting_array_function(data3)

    assert result1 == sorted_data1
    assert result2 == sorted_data2
    assert result3 == data3

    with pytest.raises(TypeError):
        sorting_array_function(data4)


if __name__ == "__main__":
    pytest.main(sys.argv)
