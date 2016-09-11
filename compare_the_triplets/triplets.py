
# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets


def compare(A, B):
    alice_points = 0
    bob_points = 0
    for i in xrange(3):
        a = A[i]
        b = B[i]
        if a > b:
            alice_points += 1
        elif a != b:
            bob_points += 1
    return (alice_points, bob_points)


if __name__ == "__main__":
    A = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())

    points = map(str, compare(A, B))

    print " ".join(points)
