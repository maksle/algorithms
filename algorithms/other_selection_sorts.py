#!/usr/bin/env python

import random
from merge_sort import merge_sort2 as merge_sort

def randomized_or_deterministic_select(a, i, n=None, type="randomized"):
    """
    input: Array a, order statistic i, length n, type either 'randomized' or
    'deterministic'
    output: value of ith smallest element
    """
    # random pivot ensures average runtime O(nlogn)
    def choosePivot(left, right):

        def deterministic_pivot():
            """
            This deterministic method of choosing a pivot is from 1973 by Blum,
            Floyd, Pratt, Rivest, and Tarjan. Outputs 'median of medians' as
            pivot. This is O(n) time despite recursive calls within (!).
            Downsides: it has worse constants in running time than randomized
            pivot and it is not in-place.
            """
            n = right - left + 1
            l = a[left:right+1]

            while len(l) > 5:
                # breaks l into chunks of 5
                l = [l[i:i+5] for i in xrange(0, n, 5)]

                # this is O(n), not O(nlogn), because each chunk is small, constant
                # time for each chunk
                l = [merge_sort(chunk) for chunk in l]
                l = [chunk[len(chunk)/2] for chunk in l]

            median_of_medians = l[len(l)/2]
            return next(i for i,v in enumerate(l) if v == median_of_medians)

        if type == "randomized":
            # Average case running time O(n) over random pivot choices. This is
            # amazing as it is only a constant times the linear time it takes to
            # read the array!
            return random.choice(range(left, right+1))
        elif type == "deterministic":
            return deterministic_pivot()

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
        return randomized_or_deterministic_select(a[:j-1], i, j-1, type)
    else: # j < i
        return randomized_or_deterministic_select(a[j:], i-j, n-j, type)

if __name__ == "__main__":
    assert randomized_or_deterministic_select([2,4,6,8,10], 3, type="deterministic") == 6
    assert randomized_or_deterministic_select([5,20,15,30,0], 2, type="randomized") == 5
    print "tests passed"
