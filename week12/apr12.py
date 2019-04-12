SOLUTION = "011"

# Calculate inner product of a and b
# For example
# 001 (.) (101) = 001
def inner_product(a, b):
	a = "{:05b}".format(int(a, 2))
	b = "{:05b}".format(int(b, 2))
	sum = 0
	for a_i, b_i in zip(a, b):
		sum += (int(a_i) * int(b_i)) % 2
	return sum % 2

# Calculate outer product of a and b
# For example
# 011 (x) (011) = 000 011 011
def outer_product(a, b):
	assert len(a) == len(b)
	product = ""
	for a_i in a:
		for b_i in b:
			product += str((int(a_i) * int(b_i)) % 2)
	return product
	

# Calculate walsh hadamard encoding
# of a binary string x
def walsh_hadamard(x):
	total = len(x)
	binarys = []
	for i in range(2**total):
		binarys.append("{:05b}".format(i))
	encoded = "".join([str(inner_product(x, b)) for b in binarys])
	return encoded


wh_u = walsh_hadamard(SOLUTION)
uxu = outer_product(SOLUTION, SOLUTION)
wh_uxu = walsh_hadamard(uxu)

print(wh_u, end='')
print(wh_uxu)