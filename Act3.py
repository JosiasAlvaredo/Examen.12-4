def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                return False
        return True

def sumValues(mat1):
    res = 0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if (i + j) %  2 != 0 and isPrime(mat1[i][j]) == True:
                res += mat1[i][j]
    return res

print(sumValues([
                [100,5,100],
                [2,100,2], 
                [100,2,100]]))
            #Los 100 son de suma de indices=numero par