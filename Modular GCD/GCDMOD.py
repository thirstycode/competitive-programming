testcases = int(input())
rem = 10**9 + 7
from math import gcd

for i in range(0,testcases):
	a,b,n = map(int,input().split())
	num2 = abs(a-b)
	if num2 != 0:
		num1a = pow(a,n,num2)
		num1b = pow(b,n,num2)
		temp = (num1a + num1b)%num2
	else:
		num1a = pow(a,n)
		num1b = pow(b,n)
		temp = num1a + num1b
	num1 = 0
	num1,num2 = num2, temp
	ans = gcd(num1,num2)%rem
	print(ans)