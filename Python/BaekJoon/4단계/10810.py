N, M = map(int, input().split())

l = [0 for i in range(N)]

for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1,j):
        l[b] = k

for i in range(N):
    print(l[i], end=' ')