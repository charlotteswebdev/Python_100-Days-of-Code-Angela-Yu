'''
My version - Prime Checker

def prime_checker(number):
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
        print("This is not a prime number.")
    else:
        print("This is a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

'''

# Angela's solution using a for loop

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)