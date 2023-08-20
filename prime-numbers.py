# Author: Brian Giblin
# Date: 8/20/23
# Description: Takes input to determine if it is a prime number.

def is_prime():
    number = int((input("Provide a number to see if it is prime:  ")))
    if number > 1:
        for i in range(2,int(number/2)+1):
            if number % i == 0:
                print(f"{number} is not a prime number")
                break

        else:
            print(f"{number} is a prime number")
    


def odd_even():
    num = int(input("Provide a number to see if it's odd or even:  "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


is_prime()
odd_even()