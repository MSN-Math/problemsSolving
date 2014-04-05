#import pdb ; pdb.set_trace()



def isPrime(n):
    if(n==2): return True
    if(n==3): return True
    if(n==5): return True
    
    sqrtN = int(n**0.5)
    for i in range(2,sqrtN):
        if ((n%i)==0):
            return False
    return True

def getNextPrime(primeFactorTab):

    if len(primeFactorTab)==0:
        primeFactorTab.append(2)
        return

    elem = primeFactorTab[len(primeFactorTab)-1]
    
    current = elem + 1
    isPrim = True
    while True:
        for prime in primeFactorTab:

            if prime > int(current**0.5):
                break

            if current%prime == 0:
                current+=1
                isPrim=False
                break

        if isPrim :
            primeFactorTab.append(current)
            return
        isPrim = True

primeFactorTab=[]
divisorsTab=[]
factor=1

cstValue=600851475143
value=cstValue
i=0

while factor < cstValue:
    getNextPrime(primeFactorTab)
    prime=primeFactorTab[i]
    
    while value%prime==0:
        factor=factor*prime
        divisorsTab.append(prime)
        value=value/prime
 
    i+=1

print("Prime factor decomposition :"+str(divisorsTab) )

