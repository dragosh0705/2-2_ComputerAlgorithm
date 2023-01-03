n, m, v = map(int, input().split())
adj = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
N = len(adj)

for _ in range(m):
  f, t = map(int, input().split())
  adj[f][t] = adj[t][f] = 1

from collections import deque

def bfs(adj, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for c in range(len(adj[value])):
        if adj[value][c] == 1 and not visited[c]:
          queue.append(c)

print('BFS 방문 순서 : ')
for i in range(N):
  if not visited[i]:
    bfs(adj, i, visited)
