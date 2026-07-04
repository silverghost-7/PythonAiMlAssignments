def ChkPrime(Num):
    for i in range(2,int(Num/2+1),1):
        if (Num%i==0):
            return False
    return True