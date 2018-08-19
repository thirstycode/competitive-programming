n = input()
n = int(n)
input_list = input().split(',')
input_list = [int(i) for i in input_list]
input_list = input_list[:n]
# print(input_list)
binary = []
for i in input_list:
	binary.append('{0:b}'.format(i))
new = []
for i in binary:
	new.append(i.count('1'))
# print(new)
# print(binary)
index = 0
ans = 0
for ele in new:
	index += 1
	for nextele in new[index:]:
		if nextele < ele:
			ans += 1
		else:
			pass
print(ans)
