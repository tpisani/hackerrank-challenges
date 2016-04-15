
# Cavity Map
# https://www.hackerrank.com/challenges/cavity-map


def cavities(M):
    n = len(M)
    c = []

    i = 1
    j = 1

    while i < n - 1:
        k = M[i][j]

        if k > M[i-1][j] and k > M[i+1][j] and k > M[i][j-1] and k > M[i][j+1]:
            c.append([i, j])

        j += 1
        if j == n - 1:
            i += 1
            j = 1

    return c


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
