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
i=0

while i < 10001:
    getNextPrime(primeFactorTab)
    prime=primeFactorTab[i] 
    i+=1

print(str(primeFactorTab[i-1]))

