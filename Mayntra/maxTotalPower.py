def maxTotalPower(N, X):
    # Current total power (1-based indexing)
    current_total = 0
    for i in range(N):
        current_total += (i + 1) * X[i]
    
    max_change = 0
    
    # Try moving each panel p to each position q
    for p in range(1, N + 1):  # p is 1-based index
        for q in range(1, N + 1):
            if p == q:
                continue
            
            if q > p:
                # sum from X[p] to X[q-1] in 0-based
                total_sum = sum(X[p:q])  # 0-based: index p to q-1
                change = (q - p) * X[p-1] - total_sum
            else:  # q < p
                # sum from X[q-1] to X[p-2] in 0-based
                total_sum = sum(X[q-1:p-1])  # 0-based: index q-1 to p-2
                change = (q - p) * X[p-1] + total_sum
            
            if change > max_change:
                max_change = change
    
    return current_total + max_change


input1 = 5
input2 = [8,1,6,3,4]
print(maxTotalPower(input1,input2))
