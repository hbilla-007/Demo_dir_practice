def myfunc(n):
    flag = False
    if n < 1:
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break
    if flag:
        print("the given no is not a prime")
    else:
        print("the given no is prime")


myfunc(11)
