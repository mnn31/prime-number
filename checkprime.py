###############################################################
# Checks if a number is prime or composite.
# If composite, scans for a prime number greater than it.
###############################################################



from math import sqrt
import time

def checkprime(orig):
    if orig == 0 or orig == 1:
        return 'Neither Prime nor composite'
    
    h = int(sqrt(orig))
    for i in range(2, h):
        if orig % i == 0:
            return f'Composite: {i} x {int(orig/i)} = {orig}'

            
    return 'Prime'
        
def greaterprime(num):
    if num % 2 == 0:
        inc = 1
    else:
        inc = 0
    while True:
        chk = num + inc
        is_prime = checkprime(chk)
        if is_prime == 'Prime':
            return chk
        else:
            inc += 2            


########################## MAIN PROGRAM ##########################
while True:
    num = int(input("Enter a number to begin scanning primes greater than that: "))
    start = time.time()
    res = greaterprime(num)
    end = time.time()
    print(f'Yay! Found prime number in {end - start} secs!')
    print(res)
        
