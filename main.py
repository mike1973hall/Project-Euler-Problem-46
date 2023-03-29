import math

def eqTwo(n, q): # sifting out divisible by two

    if (n - q) % 2 == 0:
        return True
    else: 
        return False
     
def isOdd(n): # sifting out the odd numbers

    if n % 2 == 0:
        return False
    else:
        return True

def isPrime(n): # sifting out the primes - brute force
  
    if n <= 1:
        return False
  
    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True

for n in range (0, 10000):
    
    if isPrime(n) == False and isOdd(n) == True: # finding all the odd composites
        
        for k in range (1, n):
            
            q = n - (2 * k * k) 

            if isPrime(q) == True and eqTwo(n, q) == True: #removes Goldbach composites
                break

            elif q < 0: #prints out any counter-examples
                print(n)
                break

            else:
                continue


