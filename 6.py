T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    a = x*y
    bags = a // 100
    print(bags)