
# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1


a = ord("a")
A = ord("A")


def encrypt(S, K):
    S = list(S)

    for i, c in enumerate(S):
        if "a" <= c <= "z":
            offset = a
        elif "A" <= c <= "Z":
            offset = A
        else:
            continue

        k = offset + (ord(c) - offset + K) % 26

        S[i] = chr(k)

    return "".join(S)


if __name__ == "__main__":
    N = int(raw_input().strip())
    S = raw_input().strip()
    K = int(raw_input().strip())

    print encrypt(S, K)
