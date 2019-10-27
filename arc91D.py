def main():
    n, k = map(int, input().split())

    res = 0
    for b in range(k + 1, n + 1):
        tail = max(0, (n % b) - k + 1)
        body = (b - k) * (n // b)
        res += body + tail - (k == 0)

    print(res)


if __name__ == "__main__":
    main()
