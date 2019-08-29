def find_palindrome():
	palindrome = 0
	for num1 in range(100,1000,1):
		for num2 in range(100,1000,1):
			product  = num1 * num2 
			if str(product) == str(product)[::-1]:
				if product > palindrome:
					palindrome = product
	return palindrome
print(find_palindrome())