def myfunc():
    n = int(input("enter number"))
    n1, n2 = 0, 1
    count = 0
    print("the fabinacci series")
    while count < n:
        print(n1, end=" ")
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1


myfunc()
