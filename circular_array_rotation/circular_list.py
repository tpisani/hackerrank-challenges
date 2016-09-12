
# Circular Array Rotation
# https://www.hackerrank.com/challenges/circular-array-rotation


from collections import deque


def rotate(L, k):
    circular_list = deque(L)
    circular_list.rotate(k)
    return circular_list


if __name__ == "__main__":
    n, k, q = map(int, raw_input().strip().split())
    L = map(int, raw_input().strip().split())

    rotated = rotate(L, k)

    for qi in xrange(q):
        i = int(raw_input())
        print rotated[i]
