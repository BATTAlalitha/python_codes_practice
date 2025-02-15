import math
t = int(input("Enter number of test cases: "))
for _ in range(t):
    n, x = map(int, input("Enter N (number of friends) and X (cost of one subscription): ").split())
    subscriptions_needed = math.ceil(n / 6)
    total_cost = subscriptions_needed * x
    print(f"Minimum total cost: {total_cost}")
