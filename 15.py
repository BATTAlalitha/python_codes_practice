t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    needed = max(0, n - x)  # Candies still needed
    packets = (needed + 3) // 4  # Number of packets required (each has 4 candies)
    print(packets)
