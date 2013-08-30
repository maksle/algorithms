#!/usr/bin/env python

#
# recursive version
#
def count_inversions(n):
    """
    merge-sort-count of list n; recursive version
    returns tuple: (list: <sorted list>, int: <count>)
    """
    if len(n) == 1:
        return n, 0

    mid = len(n)/2
    left, lcount = count_inversions(n[:mid])
    right, rcount = count_inversions(n[mid:])
    merged, split_inv_count = merge_count(left, right)
    return merged, lcount + rcount + split_inv_count

def merge_count(left, right, merged = None, count = None):
    """
    merge sort and count two already sorted lists; recursive version
    returns tuple: (list: <sorted list>, int: <count>)
    """
    merged = merged or []
    count = count or 0

    if left == []:
        return merged + right, count
    if right == []:
        return merged + left, count

    if left[0] <= right[0]:
        merged.append(left[0])
        return merge_count(left[1:], right, merged, count)
    else:
        merged.append(right[0])
        return merge_count(left, right[1:], merged, count + len(left))


#
# iterative version
#
def count_inversions2(n):
    """
    merge sort list n; iterative version
    returns int: <count>
    """
    stack = [[num] for num in n]
    count = 0
    tmp = []

    while True:
        slen = len(stack)
        for i in xrange(0, slen, 2):
            if i == slen - 1:
                tmp.append(stack[i])
            else:
                merged, c = merge_count2(stack[i], stack[i+1])
                count += c
                tmp.append(merged)
        stack, tmp = tmp, []
        if len(stack) == 1:
            break

    return count

def merge_count2(left, right):
    """
    merge two sorted lists; iterative version
    returns tuple: (list: <merged>, int: <count>)
    """
    len_left, len_right = len(left), len(right)
    i, j, merged, count = 0, 0, [], 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i+1
        elif right[j] < left[i]:
            count += len(left[i:])
            merged.append(right[j])
            j = j+1

    if i == len_left:
        merged += right[j:]
    if j == len_right:
        merged += left[i:]

    return merged, count
