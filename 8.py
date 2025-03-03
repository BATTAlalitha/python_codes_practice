T = int(input())  # Number of test cases
for _ in range(T):
    X = int(input())  # Amount spent
    
    if X <= 100:
        discount = 0
    elif X <= 1000:
        discount = 25
    elif X <= 5000:
        discount = 100
    else:
        discount = 500
    
    final_amount = X - discount
    print(final_amount)