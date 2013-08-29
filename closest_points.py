#!/usr/bin/env python

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<x: %d, y: %d>" % (self.x, self.y)


def dist(p1, p2):
    """
    Input: Point: <p1>, Point <p2>
    Output: float: distance between <p1> and <p2>
    """
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force(P):
    """
    Input: list: <P> of points
    Output: tuple: Point pair, float: distance
    Accepts list of points and finds pair of points with smallest distance.
    """
    lenp = len(P)
    bestp, bestd = None, float("inf")
    for i in xrange(1, lenp):
        d = dist(P[i-1], P[i])
        if d < bestd:
            bestp, bestd = (P[i-1], P[i]), d
    return bestp, bestd

def closest_points(P):
    """
    Finds closest point pair and their distance
    input P: list of Points [Pi...Pn]
    output: tuple: (point pair, distance between points)
    """
    Px = sorted(P, key=lambda p: p.x) # O(nlogn)
    Py = sorted(P, key=lambda p: p.y) # O(nlogn)

    def closest_pair(_Px, _Py):
        n = len(_Px)

        if n <= 3:
            return brute_force(_Px) # O(1)

        Qx, Qy = _Px[:n/2], _Py[:n/2] # O(n)
        Rx, Ry = _Px[n/2:], _Py[n/2:] # O(n)

        pair_l = (p1,p2), d1 = closest_pair(Qx, Qy) # T(n)/2
        pair_r = (p3,p4), d2 = closest_pair(Rx, Ry) # T(n)/2

        d = min(d1, d2)
        pair_lr = closest_split_pair(_Px, _Py, d) # O(n)

        if pair_lr is not None:
            return min(pair_l, pair_r, pair_lr, key=lambda pair: pair[1])
        return min(pair_l, pair_r, key=lambda pair: pair[1])

    def closest_split_pair(_Px, _Py, d): # O(n)
        """
        Subroutine of closest_points...
        input: list: [<Px>]. Points sorted by x attribute,
               list: [<Py>]. Points sorted by y attribute,
               float: <d>. distance
        output: tuple: (tuple: Point pair, float: distance)
          OR
        None if no pair smaller than d is found
        """
        n = len(_Px)
        if n <= 3:
            return brute_force(_Px)

        bestp, bestd = None, float("inf")

        # median line
        xm = _Px[n/2].x

        # points within range of d on either side of xm, presorted by y
        Sy = [p for p in Py if abs(xm - p.x) <= d]

        lenSy = len(Sy)
        for i in xrange(lenSy):
            j = i + 1
            # smaller pair candidate's y must be no further than d. No more than 8
            # points can exist in the d*2d space so this loop is O(1).
            while j < lenSy and Sy[i].y - Sy[j].y <= d:
                if dist(Sy[i], Sy[j]) < bestd:
                    bestp, bestd = (Sy[i], Sy[j]), dist(Sy[i], Sy[j])
                j += 1

        return bestp, bestd

    return closest_pair(Px, Py)

