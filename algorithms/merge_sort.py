#!/usr/bin/env python

#
# recursive version
#
def merge_sort(n):
    """
    merge sort of list n; recursive version
    """
    if len(n) == 1:
        return n

    mid = len(n)/2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    return merge(left, right)

def merge(left, right, merged = None):
    """
    merge two sorted lists; recursive version
    """
    merged = merged or []

    if left == []:
        return merged + right
    if right == []:
        return merged + left

    if left[0] <= right[0]:
        merged.append(left[0])
        return merge(left[1:], right, merged)
    else:
        merged.append(right[0])
        return merge(left, right[1:], merged)


#
# iterative version
#
def merge_sort2(n):
    """
    merge sort list n; iterative version
    """
    stack = [[num] for num in n]
    tmp = []
    while True:
        slen = len(stack)
        for i in xrange(0, slen, 2):
            if i == slen-1:
                tmp.append(stack[i])
            else:
                tmp.append(merge2(stack[i], stack[i+1]))
        stack, tmp = tmp, []
        if len(stack) == 1:
            break

    return stack[0]

def merge2(left, right):
    """
    merge two sorted lists; iterative version
    """
    len_left, len_right = len(left), len(right)
    i, j, merged = 0, 0, []

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i+1
        elif right[j] < left[i]:
            merged.append(right[j])
            j = j+1

    if i == len_left:
        merged += right[j:]
    if j == len_right:
        merged += left[i:]

    return merged
