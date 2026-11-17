n = int(input()) #👉 input() asks the user to type something (always returns text).
#int() converts that text into a whole number.
#The result is stored in n.



def is_prime(x): #Define a function called is_prime that takes one parameter, x


    if x < 2:
        return False  #If x is less than 2 → it is NOT prime.Return False immediately and exit the function.


    i = 2   #👉 Start testing divisors at 2. i is the number we'll divide x by.


    while i < x:   #👉 Loop while i is less than x.
#For x = 7, this will try i = 2, 3, 4, 5, 6.
#For x = 9, this will try i = 2, 3, 4, 5, 6, 7, 8.



        if x % i == 0:
            return False    #👉 x % i gives the remainder when x is divided by i.👉 == 0 means the remainder is zero → i divides x evenly.If we find any divisor, x is not prime — return False immediately.



        
        i += 1  #Move to the next divisor. 

    return True  #If the loop finished without finding any divisor, then x has no divisors other than 1 and itself → it IS prime

print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")

primes = []
total = 0
num = 2
while num <= n:   #Loop while num is less than or equal to n. For n = 10, this checks 2, 3, 4, 5, 6, 7, 8, 9, 10.

    if is_prime(num):   #If num is prime 
        primes.append(num) #Add num to the primes list
        total += num   #Add num to total
    num += 1
print(f"Primes up to {n}: {primes}")
print(f"Sum of primes: {total}")