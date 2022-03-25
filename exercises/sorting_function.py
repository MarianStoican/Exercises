# for sorting function I used the well-known quicksort algorithm with a complexity of O(nlog2n)

def sorting_array_function(data):
    def partition(low, high):
        pivot = sorted_data[high]
        index = low - 1
        for element in range(low, high):
            if sorted_data[element] <= pivot:
                index += 1
                sorted_data[index], sorted_data[element] = sorted_data[element], sorted_data[index]
        sorted_data[index + 1], sorted_data[high] = sorted_data[high], sorted_data[index + 1]

        return index + 1

    def quicksort(low, high):
        if low < high:
            index = partition(low, high)
            quicksort(low, index - 1)
            quicksort(index + 1, high)

    sorted_data = data[:]
    end = len(data) - 1

    if all(isinstance(x, int) for x in data):
        quicksort(0, end)
    else:
        raise TypeError("All elements must be integers")

    return sorted_data
