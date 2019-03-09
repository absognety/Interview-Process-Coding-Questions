def num_of_squares(n):
    if n == 1:
        return (1)
    else:
        nSquares = 0
        for I in range(1,n+1):
            nSquares = nSquares + (I*I)
        return (nSquares)
            

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n = int(input())
        print (num_of_squares(n))