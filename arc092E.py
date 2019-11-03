import numpy as np


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    sol_tot, sol_tracker = -1e10, []
    for p in range(2):
        c = a.copy()

        idx = np.arange(p, n, 2)
        if len(idx) == 0:
            continue

        pick = max(idx, key=lambda x: c[x])
        chosen = {pick} \
            if c[pick] <= 0 \
            else {x for x in idx if c[x] > 0}

        is_chosen, tot, tracker = [False] * n, 0, []
        for i in chosen:
            tot += c[i]
            is_chosen[i] = True

        for i in reversed(range(n)):
            if not is_chosen[i]:
                if i == 0 or i + 1 == len(c):
                    tracker += [i]
                    del c[i], is_chosen[i]
                elif is_chosen[i - 1] == is_chosen[i + 1]:
                    tracker += [i]
                    c[i - 1] += c[i + 1]
                    del c[i + 1], c[i], is_chosen[i + 1], is_chosen[i]

        if len(c) > 1 and not is_chosen[0]:
            tracker += [0]
            del c[0], is_chosen[0]

        if tot > sol_tot:
            sol_tot, sol_tracker = tot, np.array(tracker) + 1

    print(sol_tot, len(sol_tracker), *sol_tracker, sep='\n')


if __name__ == '__main__':
    main()
