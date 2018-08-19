def determine(a,b,c,x,y):
	k = x - b
	if c+a-k == y and 0 <= k <= a:
		return True
	k = x - c
	if b+a-k == y and 0 <= k <= a:
		return True
	k = y - b
	if c+a-k == x and 0 <= k <= a:
		return True
	k = y - c
	if b+a-k == x and 0 <= k <= a:
		return True
	return False




test = int(input())
for i in range(0,test):
	result = False
	a,b,c,x,y = map(int,input().split(" "))
	result = determine(a,b,c,x,y)
	if result == False:
		result = determine(b,a,c,x,y)
	if result == False:
		result = determine(c,a,b,x,y)
	if result == True:
		print("YES")
	else:
		print("NO")
