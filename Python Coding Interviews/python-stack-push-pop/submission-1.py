from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    result = arr.copy()
    left, right = 0, len(result) - 1
    while left < right:
        result[left], result[right] = result[right],result[left]
        left += 1
        right -= 1
    return result


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
