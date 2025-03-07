T = int(input())
for i in range(T):
    referees = map(int,input().split()) #r1,r2,r3,r4
    if all(r == 0 for r in referees):
        print("IN")
    else:
        print("OUT")