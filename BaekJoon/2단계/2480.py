num = list(map(int, input().split()))

num.sort(reverse=True)

if (num[0] == num[2]):
    print(10000 + (num[0]*1000))
elif num[0]!=num[1]!=num[2]:
    print(num[0]*100)
else:
    if num[0]==num[1]:
        print(1000 + (num[0]*100))
    else:
        print(1000 + (num[1]*100))

