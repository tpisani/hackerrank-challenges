#!/bin/python

# https://www.hackerrank.com/challenges/the-grid-search

def search(G, P):
    R = len(G)
    r = len(P)

    i = 0
    j = 0
    k = 0

    while i < R and j < r:
        try:
            k = G[i+j].find(P[j])
        except IndexError:
            break

        if k != -1:
            j += 1
        else:
            i += 1
            j = 0
            k = 0

    if j == r:
        return True
    return False


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
