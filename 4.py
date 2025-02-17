t = int(input("enter the number of test cases:"))
for _ in range(t):
    x,y,z= map(int,input().split())
    test_passed = x * y
    if z > (test_passed / 2):
        print("YES")
    else:
        print("NO")
    