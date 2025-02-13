f = open("input.txt", "r")
count = 0
for i in f:
	j=list(map(int, i.split()))

	if j[0] > j[1]:
		m = -1
	elif j[0] < j [1]:
		m = 1
	else:
		continue

	for x in range(len(j) -1):
		if 0 < (j[x + 1] -j [x] ) * m < 4:
			t = True
		else:
			t = False
			break

	if t:
		count += 1

print(count)