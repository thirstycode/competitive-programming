from math import log
import string

testcases = int(input())
for i in range(0,testcases):
	n = int(input())
	binary = "{0:b}".format(n)
	count = 0
	for char in binary:
		if char == '1':
			count += 1
		else:
			pass
	if count == 2:
		print(0)
	elif count == 1 and n != 1:
		print(1)
	elif count == 1 and n == 1:
		print(2)
	elif count == 0:
		print(3)
	else:
		rev = binary[::-1]

		# print(binary)
		
		lower = rev.replace('1','0',count-2)[::-1]
		lower = int(lower,2)
		# print(lower)
		index = 0
		count1 = 0
		for char in binary:
			if count1 < 2:
				if char == '1':
					count1 += 1
				else:
					pass
			else:
				break
			index += 1
		index -= 1
		if '0' == binary[index-1]:
			# print('here')
			binary = binary.replace('01','10',1)
			rev = binary[::-1]
			rev = rev.replace('1','0',count-2)
			binary = rev[::-1]
			upper = int(binary,2)
		else:
			leng = len(binary)
			binary = '1' + '0'*(leng-1) + '1'
			upper = int(binary,2)

		# print(binary)
		
		diff = min(abs(upper-n),abs(lower-n))
		print(diff)
