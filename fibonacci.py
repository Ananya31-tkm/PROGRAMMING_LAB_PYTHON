def Fibonacci_series(n1,n2):
    n3=n1+1
    if(n2 <= n1):
        print("enter valid range:")
    elif(n2 == 1):
        return 1
    else:
        ls=[]
        while n1<=n2:
            ls.append(n1)
            nth=n1+n3
            n1=n3
            n3=nth
        return ls


