def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
        return True


print("prime Numbers")
def printPrime(n):
    sb =[0,1]
    for i in range(2, n+1):
        if is_prime(i):
            sb.append(i)
    return sb

list1=printPrime(10)
print(list1)
