import math

def is_prime(n):
    return not any(n % p == 0 for p in range(2, int(math.sqrt(n)) + 1))

t = int(input())
for i in range(0,t):
	x,y = map(int,input().split(" "))
	num = x + y
	ans = num + 1
	while(is_prime(ans) == False):
		ans += 1
	print(ans-num)
