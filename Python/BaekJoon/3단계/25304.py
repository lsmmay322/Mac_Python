Price = int(input())
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    Price = Price - (a*b)

if Price == 0:
    print('Yes')
else:
    print('No')