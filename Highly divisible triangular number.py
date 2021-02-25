from sympy import factorint
def number_of_divisors(n):
	prime_factors=factorint(n)
	mul=1
	for i in prime_factors.values():
		mul*=i+1
	return mul

def generate_triangle_number():
	n=1
	while True:
		t=(n*(n+1))//2
		if number_of_divisors(t)>500:
			return t
		else:
			n+=1

print(generate_triangle_number())


