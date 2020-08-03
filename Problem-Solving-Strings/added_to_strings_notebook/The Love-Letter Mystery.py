# minimum number of operations needed to make the string a palindrome
# He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
# The letter a may not be reduced any further
def minimum_reductions(s):
	n = len(s)
	count = 0
	for i in range(n // 2):
		left = ord(s[i])
		right = ord(s[(n - 1) - i])
		if left != right:
			if left > right:
				count += left - right
			else:
				count += right - left
	return count


T = int(input())
for _ in range(T):
	s = input()
	print(minimum_reductions(s))

