# to find next permutation I used this algorithm:
#   1. find the highest index i such that s[i] < s[i+1] (If no such index exists, the permutation is
#   the last permutation.)
#   2. find the highest index j > i such that s[j] > s[i]. Such a j must exist, since i+1 is such
#   an index.
#   3. swap s[i] with s[j].
#   4. reverse the order of all of the elements after index i till the last element

def next_alphabetical_permutation(chars_list):
    if not all(isinstance(char, str) and char.isalnum() for char in chars_list):
        return 'The input must be a sequence of alphabetical chars'
    if len(chars_list) < 2:
        return chars_list
    int_list = [ord(char) for char in chars_list]
    index = -1
    for i in reversed(range(1, len(int_list))):
        if int_list[i - 1] < int_list[i]:
            index = i - 1
            break
        if i == 1:
            return [*reversed(chars_list)]

    for i in reversed(range(index, len(int_list))):
        if int_list[i] > int_list[index]:
            int_list[i], int_list[index] = int_list[index], int_list[i]
            new_list = int_list[:index + 1] + int_list[index + 1:][::-1]
            return [chr(x) for x in new_list]
