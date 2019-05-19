from random import randrange, getrandbits
import sys
sys.setrecursionlimit(10**6)

def gcd(a,b):
	if b == 0:
		return(a)
	else:
		d=gcd(b,a%b)
	return(d)
	
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
	
def gyorshatvany(g,e,p):
	mod=1
	tmp=g%p
	while e != 1:
		if e%2 == 1:
			mod=(mod*tmp)%p
		tmp=(tmp**2)%p
		e //= 2
	mod*=tmp
	return mod%p

def is_prime(n, k=128):
  
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r%2 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = gyorshatvany(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = gyorshatvany(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False

    return True

def generate_prime_candidate(length):
   
    p = getrandbits(length)
    p |= (1 << length - 1) | 1

    return p

def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p
	
def gen_e(phin):
	e=0
	while gcd(phin,e)!= 1:
		e=randrange(2,100)
		if e%2 == 0:
			e=e-1
	return(e)
	
def crt(p,q,d,c):
	c1=gyorshatvany(c,d%(p-1),p)
	c2=gyorshatvany(c,d%(q-1),q)
	M=p*q
	b,x0,y0=xgcd(p,q)
	y1,y2=x0,y0
	print((y1*p)%q)
	print((y2*q)%p)
	return (c1*y1*p+c2*y2*q)%M
	

	
	
p = generate_prime_number()
q = generate_prime_number()
n = p*q
phin = (p-1) * (q-1)
e = gen_e(phin)

d = xgcd(phin,e)[2]

m=26

m=gyorshatvany(m,e,n)

m=crt(p,q,d,m)
print(m)










