#!/usr/bin/env python

import random

def quicksort(a, left=0, right=None):
    """
    In-place implementation for O(n) memory, O(nlogn) average case runtime
    Takes list of numbers and outputs the sorted mutated list.
    """

    def partition(a, left, right):

        # random pivot ensures average runtime O(nlogn)
        def choosePivot():
            return random.choice(range(left, right+1))

        p = choosePivot()

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

    right = right or len(a)-1
    n = right-left + 1

    # base case, where length of 1 is sorted
    if n <= 1:
        return a

    p = partition(a, left, right)
    quicksort(a, left, p-1)
    quicksort(a, p+1, right)

    return a

if __name__ == "__main__":
    print quicksort([1,9,10,2,4,5,10,8,7,3,6,10])
