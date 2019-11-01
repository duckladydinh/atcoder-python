from bisect import bisect_left
import numpy as np


def main():
    n = int(input())
    a = np.array([int(x) for x in input().split()])
    b = np.array([int(x) for x in input().split()])

    N, res = 30, 0
    for i in range(N):
        T, ones = 1 << i, 0
        c = sorted(b % (T + T))

        for x in (a % (T + T)):
            cnt = [bisect_left(c, T * k - x) for k in range(1, 4)]
            ones += (cnt[1] - cnt[0]) + (n - cnt[2])

        res += T if ones % 2 == 1 else 0

    print(res)


if __name__ == '__main__':
    main()
