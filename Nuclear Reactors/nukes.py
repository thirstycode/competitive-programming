a,n,k = map(int,input().split(" "))
particles = [0]*k
for i in range(0,k):
	particles[i] = a%(n+1)
	a = int(a/(n+1))

print(*particles,sep=" ")