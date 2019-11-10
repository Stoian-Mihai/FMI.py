def z(i,j,n):
    nr = 0
    if n == 0:
        return 1
    else:
        if i > n:
            nr = nr + 2 * n * n
            i = i-n
        if j > n:
            nr = nr + n * n
            j  = j-n
        return nr + z(i, j, int(n/2))

n = 2
i = 3
j = 3
dim = (2**n)
print(dim)
print(z(i,j,dim))