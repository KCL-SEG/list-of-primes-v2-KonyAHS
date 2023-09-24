"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    
    #dealing with exceptions
    if number_of_primes >0:
        list = [2]
    else:
        raise ValueError("The numbers of primes requested is lower than 1, please enter a valid number")
        
    currentNumber = 3
    prime = True
    while len(list) < number_of_primes:    
        
        #checking the odd demonirators
        for divider in range(3,currentNumber//2,2):
            if currentNumber%divider == 0:
                prime = False
                break
            
        #adding to list
        if prime:
            list.append(currentNumber)    
        
        #resetting condition
        currentNumber+=2
        prime = True
                
    return list