N, M = map(int, input().split())

ball_list = list(range(1,N+1))

for i in range(M):
    x, y = map(int, input().split())
    ball_list[x-1], ball_list[y-1] = ball_list[y-1], ball_list[x-1]

for i in range(N):
    print(ball_list[i], end=' ')