
# Cavity Map
# https://www.hackerrank.com/challenges/cavity-map


def cavities(M):
    return []


if __name__ == "__main__":
    n = int(raw_input().strip())
    M = []
    for i in xrange(n):
        r = raw_input().strip()
        M.append(map(int, list(r)))

    for i, j in cavities(M):
        M[i][j] = "X"

    for r in M:
        print "".join(str(c) for c in r)
