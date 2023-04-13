a = []

for i in range(9):
    n = int(input())
    a.append(n)

max = a[0]
max_n = 1

for i in range(9):
    if a[i] > max:
        max = a[i]
        max_n = i+1

print(max)
print(max_n)