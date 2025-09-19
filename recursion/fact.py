def fact(num):
    if num==0:
        return 1
    else:
       return num * fact(num-1)


print(fact(5))


def fibbo(n):
    if n<=0:
        return "Enter Positive Number"
    elif n==1:

        return 0
    elif n==2:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)

n = int(input("Enter the number for fibbonacci series"))

print("fibonacci series")
for i in range(1,n+1):
    print(fibbo(i),end=" ")





