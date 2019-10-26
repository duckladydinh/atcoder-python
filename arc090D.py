import networkx as nx
import networkx.utils as nxs
import numpy as np


def main():
    N, M = map(int, input().split())
    edges = [[int(x) for x in input().split()] for _ in range(M)]

    U = nxs.UnionFind()
    G = nx.DiGraph()

    for e in edges:
        if e[2] == 0:
            U.union(e[0], e[1])

    is_possible = True
    for e in edges:
        if U[e[0]] == U[e[1]]:
            is_possible &= e[2] == 0
        else:
            G.add_edge(U[e[0]], U[e[1]], weight=e[2])

    is_possible = nx.is_directed_acyclic_graph(G) and verify(G, N)

    print('Yes' if is_possible else 'No')


def verify(G, N):
    d = np.zeros(N + 1, dtype=np.int)
    for x in nx.topological_sort(G):
        is_first = True
        for (y, _) in G.in_edges(x):
            w = G[y][x]['weight']

            if is_first:
                is_first = False
                d[x] = d[y] + w
            elif d[x] != d[y] + w:
                return False
    return True


if __name__ == "__main__":
    main()
