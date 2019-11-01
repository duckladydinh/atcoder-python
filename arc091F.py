def main():
    n = int(input())
    res = 0
    for (a, k) in [map(int, input().split()) for _ in range(n)]:
        while a > k and a % k != 0:
            m = a // k
            x = (a - k * m - 1) // (m + 1)
            a -= max(1, x) * (m + 1)
        res ^= a // k
    print('Takahashi' if res != 0 else 'Aoki')


if __name__ == '__main__':
    main()
