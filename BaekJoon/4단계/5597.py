Grade = [0 for i in range(31)]

for i in range(28):
    num = int(input())
    Grade[num] = Grade[num]+1

for i in range(1, 31):
    if Grade[i] == 0:
        print(i)