def practice(n):
    print(n)

    if n == 1:
        return n
    
    else:
        if n % 2 == 1:
            practice(3*n+1)
        else:
            practice(n//2)




if __name__ == "__main__":
    practice(3)