len = input()
for bluh in range(int(len)):
	x, y = input().split(" ")
	for n in range(int(x), int(y)+1):
		if n < 2:
			prime = False
		else:
			prime = True
		div = 1
		for i in range(2, int(n/div)):
			if (n%i==0):
				prime = False
				break
			div = div + 1
		if prime == True:
			print(n)
	print('\n')