#!/usr/bin/env python

import random

def randomized_select(a, i, n=None):
    """
    input: Array a, order statistic i, length n
    output: value of ith smallest element

    Average case running time O(n) over random pivot choices. This is amazing
    as it is only a constant times the linear time it takes to read the array!
    """
    # random pivot ensures average runtime O(nlogn)
    def choosePivot(left, right):
        return random.choice(range(left, right+1))

    # mostly borrowed from the quicksort implementation, minor changes
    # todo: combine implementations
    def partition(a, left=None, right=None, p=None):
        """
        Subroutine that does the brunt of the work.
        Outputs index of pivot p: [ <p | p | >p ]
        The <p and >p partitions may or may not be sorted.
        """

        left = left or 0
        right = right or len(a)-1
        p = choosePivot(left, right) if p is None else p

        # swap pivot value out of the way
        a[left], a[p] = a[p], a[left]
        pval = a[left]

        # a[left+1]...a[i-1] are all <= pval
        # a[i]...a[j-1] are all > pval
        i = left + 1

        for j in range(left+1, right+1):
            if a[j] < pval:
                a[j], a[i] = a[i], a[j]
                i += 1

        # swap pivot value to it's 'rightful' place
        a[left], a[i-1] = a[i-1], a[left]
        return i-1

    n = n or len(a)

    if n == 1:
        return a[i-1]

    p = choosePivot(0, len(a)-1)
    j = partition(a, p=p) + 1

    if j == i:
        return a[j-1]
    elif j > i:
        return randomized_select(a[:j-1], i, j-1)
    else: # j < i
        return randomized_select(a[j:], i-j, n-j)

if __name__ == "__main__":
    print randomized_select([4,3,2,1], 3)
