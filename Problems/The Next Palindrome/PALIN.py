testcases = int(input())

# def is_palindrome(num):
# 	num = str(num)
# 	if num == num[::-1]:
# 		return True
# 	else:
# 		return False

def incre(num):
	leng = len(num)
	carry = 1
	num_zer = 0
	while(carry == 1):
		digit = int(num[-1])
		if digit == 9:
			carry = 1
			num_zer += 1
			if num_zer < leng:
				num = num[:-1]
			else:
				return '1' + '0'*num_zer,True
		else:
			num = num[:-1] + str(digit + 1)
			carry = 0
	if num_zer > 0:
		return num + '0'*num_zer,False
	else:
		return num,False

def find_palindrome(num):
	numstr = num
	leng = len(numstr)
	oddeven = leng%2
	mid = int(leng/2)

	if len(num) == 1 :
		if num != '9':
			return str(int(num)+1)
		else:
			return '11'

	#case 1: if alredy palindrome
	# status = is_palindrome(num)
	# if status == True:
	# 	if oddeven == 0:
	# 		half = numstr[:mid] ; half = int(half)
	# 		half += 1
	# 		strhalf = str(half)
	# 		fullstring = strhalf + strhalf[::-1] ; fullstring = int(fullstring)
	# 		return fullstring
	# 	else:
	# 		half = numstr[:mid + 1 ] ; half = int(half)
	# 		half += 1	
	# 		strhalf = str(half)
	# 		fullstring = strhalf[:-1] + strhalf[::-1] ; fullstring = int(fullstring)
	# 		return fullstring

	# case 2 : if its not palindrome
	# subcase 1: direct mirroring from left to right is ok and subcase 2 : mirror is small than actual number
	if oddeven == 0:
		half = numstr[:mid]
		fullstring = half + half[::-1]
		if fullstring > numstr: #subcase1
			return fullstring
		else:  #subcase2
			strhalf,special = incre(half)
			if special:
				return '1' + '0'*(leng-1) + '1'
			else:
				return strhalf + strhalf[::-1]
	# subcase 2
	else: 
		half = numstr[:mid + 1 ]
		fullstring = half[:-1] + half[::-1]
		if fullstring > numstr: #subcase1
			return fullstring
		else:  #subcase2
			strhalf,special = incre(half)
			if special:
				return '1' + '0'*(leng-1) + '1'
			else:
				return strhalf[:-1] + strhalf[::-1]

for i in range(0,testcases):
	x = input()
	print(find_palindrome(x))
