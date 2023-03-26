a, b = map(int, input().split())
c = int(input())

c_h = int(c/60)
c_m = c%60

if c_m + b >= 60:
    if (a+c_h+1) > 23:
        print((a+c_h+1)-24, c_m+b-60)
    else:
        print(a+c_h+1, c_m+b-60)
else:
    if (a+c_h) > 23:
        print((c_h+a)-24, c_m+b)
    else:
        print(a+c_h, c_m+b)