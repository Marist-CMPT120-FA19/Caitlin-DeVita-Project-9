#Caitlin De Vita
#caitlin.devita1@marist.edu
#Sieve of Eratosthenes alorithm (finds all of the prime numbers up to some limit n)

def main():
    n = int(input("Enter a number n to find all the primes less than or equal to n: "))
    numbers = []
    for i in range(2 , n+1):
        numbers.append(i)
        
    while len(numbers) > 0:
        prime = numbers.pop(0)
        print(prime , "is prime.")
        
        for x in numbers:
            if x % prime == 0:
                numbers.remove(x)
        
main()
