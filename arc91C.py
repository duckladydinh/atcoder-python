def main():
    n, m = map(int, input().split())
    print(compute(min(n, m), max(n, m)))


def compute(n, m):
    if n == 1 and m == 1:
        return 1
    if n == 1:
        return max(0, m - 2)
    return (n - 2) * (m - 2)


if __name__ == "__main__":
    main()
