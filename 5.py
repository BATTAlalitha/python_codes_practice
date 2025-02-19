T = int(input())  # Number of test cases

for _ in range(T):
    X, Y = map(int, input().split())  # Read X and Y
    total_hours = (4 * X) + Y  # Calculate total working hours in a week
    print(total_hours)
