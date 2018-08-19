import sys

sol_list = {} #to reduce the recursive computation #really nice trick

def sol(num):
	if num <=	11:
		return num
	if num in sol_list.keys():
		return sol_list[num]
	else:
		sol_list[num] = sol(int(num/2)) + sol(int(num/3)) + sol(int(num/4))
		return sol_list[num]

try:
	while True:
	    i = int(input())
	    print(sol(i))
except :
    sys.exit(0)
