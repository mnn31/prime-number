###############################################################
# Checks if a numebr is prime or composite.
###############################################################

#CONSTANTS


def checkprime(orig):
    if orig == 0 or orig == 1:
        return 'Neither Prime nor composite'
    
    h = int(orig/2)
    for i in range(2, h):
        if orig % i == 0:
            return f'Composite: {i} x {int(orig/i)} = {orig}'

            
    return 'Prime'
        

#def test():
#   for num in range(100):
#      res = checkprime(num)
#     print(num, 'is', res)




########################## MAIN PROGRAM ##########################
while True:
    num = int(input("Enter a number: "))
    res = checkprime(num)
    print(res)

        
