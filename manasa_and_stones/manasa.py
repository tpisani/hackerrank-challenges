
# Manasa and Stones
# https://www.hackerrank.com/challenges/manasa-and-stones


def guess_stones(n, a, b):
    if a == b:
        return [(n - 1) * a]

    if a > b:
        a, b = b, a

    stones = []
    for i in xrange(n):
        stone = ((n - 1 - i) * a) + (i * b)
        stones.append(stone)
    return stones


if __name__ == "__main__":
    T = int(raw_input().strip())
    for t in xrange(T):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        stones = guess_stones(n, a, b)
        print " ".join(str(s) for s in stones)
