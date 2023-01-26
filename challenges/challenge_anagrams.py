def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())

    merge_sort(first)
    merge_sort(second)

    first_result = ''.join(first)
    second_result = ''.join(second)
    anagram = first_result == second_result

    if not first_string or not second_string:
        return (first_result, second_result, False)

    return (first_result, second_result, anagram)


def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)

    if end - start > 1:
        middle = (start + end) // 2
        merge_sort(string, start, middle)
        merge_sort(string, middle, end)
        merge(string, start, middle, end)


def merge(string, start, middle, end):
    left = string[start:middle]
    right = string[middle:end]

    left_index = 0
    right_index = 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index += 1
        else:
            string[general_index] = right[right_index]
            right_index += 1
