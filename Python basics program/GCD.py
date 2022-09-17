a=int(input())
b=int(input())


while a!=0:
    a,b=b%a,a
print("The GCD :",b)