t = int(input("Enter number of test cases: "))  # Read the number of test cases

inputs = [
    "5",
    "5 9 6",
    "5 8 6",
    "5 7 6",
    "4 9 8",
    "3 7 2"
]

for _ in range(t):
    a, b, c = map(int, inputs[_ + 1].split())  # Read A, B, and C from predefined inputs
    
    avg = (a + b) / 2  # Compute the average of A and B
    
    if avg > c:  # Check if the average is strictly greater than C
        print("YES")
    else:
        print("NO")
