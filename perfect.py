n = int(input("enter number"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum+i
if sum == n:
    print("the given number is a  perfect number")
else:
    print("the given number is not a perfect number")
