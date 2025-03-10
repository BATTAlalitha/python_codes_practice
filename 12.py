T = int(input())  # Number of test cases

for i in range(T):
    A, B, X, Y = map(int, input().split())  # Read A, B, X, Y for each test case
    m = A * B  # Required power
    n = X * Y  # Available power
    
    if n >= m:
        print("Yes")  # Use "Yes" instead of "yes" for consistency
    else:
        print("No")  # Use "No" instead of "no" for consistency
