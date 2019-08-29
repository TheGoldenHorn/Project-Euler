a = 0
b = 1
sum = 0
add=0
while (sum<=4*(10**6)):
	sum = a + b
	if(sum%2==0):
		print(sum)
		add+=sum
	#print(sum)
	b=a+b
	a = b-a 

	print(add)