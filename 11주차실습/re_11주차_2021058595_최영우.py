def bfs(i):
    queue = [] # 큐 선언 (리스트로 큐 구현)
    visited[i] = True
    queue.append(i) # 큐에 시작정점 삽입
    while len(queue) != 0:
        v = queue.pop(0) # 큐에서 정점 v를 가져옴
        print(v) # 정점 v 출력
        for w in range(1,n+1): # 정점 v에 인접한 방문 안된 정점에 대해
            if alist[v][w] and not visited[w]:
                visited[w] = True
                queue.append(w) # v에 인접한 정점을 큐에 삽입

n, m, s = list(map(int,input().split(' ')))
alist = [[0] * (n+1) for _ in range(n+1)]
N = len(alist)
visited = [None] * N


for i in range(m):
    edge_a,edge_b = map(int,input().split())
    alist[edge_a][edge_b] = 1
    alist[edge_b][edge_a] = 1

#print(alist)
bfs(s)
