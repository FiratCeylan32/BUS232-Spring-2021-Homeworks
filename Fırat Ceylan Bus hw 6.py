def isPrime(n) :
    if(n<=1) :
        return False
    if(n<=3) :
        return True
    if(n%2==0 or n%3==0) :
        return False
 
    i=5
    while(i*i<=n) :
        if(n%i==0 or n%(i+2)==0) :
            return False
        i=i+6
    return True

def first_20_primes():
    res=[]
    i=0
    while(1):
        if(len(res)==20):
            break
        else:
            if(isPrime(i)):
                res.append(i)
            i+=1
    return res

def first_19_fake_primes(primes20):
    fakeprimes=[]
    for i in range(1,20):
        fakeprimes.append(primes20[i]*primes20[i-1])
    return fakeprimes

first20primes=first_20_primes()

first19fakeprimes=first_19_fake_primes(first20primes)
print("List of first 20 primes :"+str(first20primes))
print("List of first 19 fake primes : "+str(first19fakeprimes))