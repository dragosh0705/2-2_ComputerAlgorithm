def dfs(v):
    visited[v] = True
    print(v)
    adj_list[v].sort()
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


n, m, s = map(int, input().split())

adj_list = [[-1]] + [[] for _ in range(n)]
num = len(adj_list)
visited = [None] * num


for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

print('[DFS 방문 순서]')
dfs(s)