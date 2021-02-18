# Ulam Spiral in python
n = int(input())
T = []
for i in range(n):
    temp = [0]*n
    T.append(temp)
T[n//2][n//2] = 1
i = 0
while n > 1:
    T[i][i] = n*(n-1)+1
    T[i][n - 1 + i] = n**2
    
    # First Horizontal
    k = n - 2 + i
    while k >= i:
        T[i][k] = T[i][k+1]-1
        k -= 1
    
    # First Vertical
    k = i
    l = i + 1
    while l <= n - 1 + i:
        T[l][k] = T[l-1][k] - 1
        l += 1
    
    # Second Horizontal
    l -= 1
    k = i + 1
    while k <= n - 1 + i:
        T[l][k] = T[l][k-1]-1
        k += 1
    
    # Second Vertical
    l = n - 2 + i
    k -= 1
    while l > i:
        T[l][k] = T[l+1][k] - 1
        l -= 1
    n -= 2
    i+=1
    
for i in T:
    print(' '.join(f'{x:02}' for x in i)) # Apenas fica formatado para n <= 9
