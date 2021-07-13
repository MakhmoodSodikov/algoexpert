"""
Given: [3, 5, -4, 8, 11, 1, -1, 6], 10
Answer: [11, -1]

Find two numbers from given array which sum is equal to given number
"""


def first_solution(array, target_sum):
    """
    O(N^2) -- time
    O(1) -- space
    """

    ret = []
    flag = False

    for elem1 in array:
        for elem2 in array:
            if elem2 + elem1 == target_sum and elem2 != elem1 and not flag:
                ret.append(elem1)
                ret.append(elem2)
                flag = True

    return ret


def second_solution(array, target_sum):
    """
    O(N) -- time
    O(N) -- space
    """

    hash_map = {}

    for elem in array:
        diff = target_sum - elem

        if diff not in hash_map:
            hash_map[elem] = True
        else:
            return [diff, elem]


def third_solution(array, target_sum):
    """
    O(NlogN) -- time
    O(1) -- space
    """

    left = 0
    right = len(array) - 1
    array = sorted(array)

    while True:
        sum = array[right] + array[left]

        if sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
        else:
            return [array[right], array[left]]


example_inp = ([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(first_solution(*example_inp))
print(second_solution(*example_inp))
print(third_solution(*example_inp))
