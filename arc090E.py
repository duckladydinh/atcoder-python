import networkx as nx
import numpy as np

MOD = 10 ** 9 + 7


def main():
    n, m = map(int, input().split())
    src, dst = map(int, input().split())

    G = nx.Graph()
    for _ in range(m):
        x, y, z = map(int, input().split())
        G.add_edge(x, y, weight=z)

    src_dist = nx.single_source_dijkstra_path_length(G, src, weight='weight')
    dst_dist = nx.single_source_dijkstra_path_length(G, dst, weight='weight')
    tot_dist = src_dist[dst]

    src_cnt = np.zeros(n + 1, dtype=np.int)
    dst_cnt = np.zeros(n + 1, dtype=np.int)

    src_cnt[src] = 1
    dst_cnt[dst] = 1
    for (dist, other_dist, cnt) in ((src_dist, dst_dist, src_cnt), (dst_dist, src_dist, dst_cnt)):
        ordered_vertexes = sorted(range(1, n + 1), key=lambda x: dist[x])
        for x in ordered_vertexes:
            for (y, data) in G[x].items():
                z = data['weight']
                if dist[y] + z + other_dist[x] == tot_dist:
                    cnt[x] = (cnt[x] + cnt[y]) % MOD

    res = 0
    for x in range(1, n + 1):
        if src_dist[x] == dst_dist[x] and src_dist[x] + dst_dist[x] == tot_dist:
            tmp = ((src_cnt[x] * dst_cnt[x] % MOD) ** 2) % MOD
            res = (res + tmp) % MOD

    for x in range(1, n + 1):
        for (y, data) in G[x].items():
            z = data['weight']
            if src_dist[x] * 2 < tot_dist and dst_dist[y] * 2 < tot_dist and src_dist[x] + dst_dist[y] + z == tot_dist:
                tmp = ((src_cnt[x] * dst_cnt[y] % MOD) ** 2) % MOD
                res = (res + tmp) % MOD

    res = (src_cnt[dst] * src_cnt[dst] % MOD + MOD - res) % MOD
    print(res)


if __name__ == "__main__":
    main()
