#!/bin/python

# https://www.hackerrank.com/challenges/the-grid-search


def search(G, P):
    R = len(G)
    r = len(P)

    i = 0
    j = 0
    l = 0
    m = -1

    while i < R and j < r:
        try:
            k = G[i+j][l:].find(P[j])
        except IndexError:
            break

        if m == -1:
            m = k

        if k != -1:
            if k == m:
                j += 1
            else:
                j = 0
                l += 1
                m = -1
        else:
            i += 1
            j = 0
            l = 0
            m = -1

    return j == r


if __name__ == "__main__":
    T = int(raw_input().strip())

    for t in xrange(T):
        G = []
        R, C = map(int, raw_input().strip().split())
        for _ in xrange(R):
            G.append(raw_input().strip())

        P = []
        r, c = map(int, raw_input().strip().split())
        for _ in xrange(r):
            P.append(raw_input().strip())

        if search(G, P):
            print "YES"
        else:
            print "NO"
