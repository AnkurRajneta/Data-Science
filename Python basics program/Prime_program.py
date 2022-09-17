def isprime(n):
## Search for factor in the range[2,sqrt(n)]
##sq=n**(1/2)
   
    sq=int(n**(1/2))
    
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

print(isprime(25))
