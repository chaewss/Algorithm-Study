import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(i, j, k):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if region[nx][ny] > k and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


N = int(sys.stdin.readline())
region = []
region_value = {0}
for _ in range(N):
    small_region = list(map(int, sys.stdin.readline().split()))
    region_value.update(small_region)
    region.append(small_region)


answer = 0
for k in region_value:
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if region[i][j] > k and not visited[i][j]:
                count += 1
                bfs(i, j, k)
    answer = max(answer, count)
print(answer)