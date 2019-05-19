import random
import math

minPrime=2;
maxPrime=123701;

#function to check if the given number is prime
def isPrime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0:
			return False
	return True

# creating an array of prime numbers
primes = [i for i in range(minPrime, maxPrime) if isPrime(i)]

#generating two prime numbers from our array
p = random.choice(primes)
q = random.choice(primes)

if p != q:
	n = p * q # First part of the public key

#Euclid's algorithm for determining the greatest common divisor

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

e = 2;
phi = (p-1)*(q-1)


while e < phi:
	if gcd(e,phi):
		break
	else:
	  	e = e+1




#Calculating the Private key
k = random.randint(1,10)
d = (k*phi + 1)/e


#get text from input
message = 89 # HI
#assign each letter a number
''' A:1
	B:2
	C:3
	.
	.
	.
	Z:26
'''

#encryption
c = (message**e)%n
print(c)

#decryption
m = (c**d) % n

print("Original message was {0}".format(m))

#encrypted data c=(text)^e mod n
#decrypted data = c^d mod n
