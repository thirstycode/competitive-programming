p,s = map(int,input().split())
scores = {}
solves = {}
for i in range(1,p+1):
	scoretemp = list(map(int,input().split()))
	solvetemp = list(map(int,input().split()))
	solvetemp = [solvetemp for _,solvetemp in sorted(zip(scoretemp,solvetemp))]
	scores[i] = sorted(scoretemp)
	solves[i] = solvetemp
nandi = []
for i in range(1,p+1):
	n = 0
	solve_list = solves[i]
	for pre,nex in zip(solve_list,solve_list[1:]):
		if pre > nex:
			n += 1
		else:
			pass
	nandi.append([n,i])
# print(scores)
# print(solves)
# print(nandi)
for key in sorted(nandi):
	print(key[1])
