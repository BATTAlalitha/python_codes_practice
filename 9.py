import math
T = int(input())
for i in range(T):
    n,x = map(int,input().split())
    d = n*x
    a =math.ceil(d/4)
    print(a)