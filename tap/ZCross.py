
t_dim_2 = [[1, 2], [3, 4]]

def z(i, j, dim):
    t = dim ** 2
    if dim == 2:
        return t_dim_2[i-1][j-1]

    d = dim//2
    if i <= d: # I or II
        if j <= d:
            return z(i, j, d) #I
        else:
            j -= d
            return t//4 + z(i, j, d) # II
    else: # III or IV
        if j <=d:
            i -= d
            return t//2 + z(i, j, d) # III
        else:
            i -= d
            j -= d
            return 3*t//4 + z(i, j, d) # IV
n = 2
i = 3
j = 3
dim = 2**n
print(z(i,j,dim))