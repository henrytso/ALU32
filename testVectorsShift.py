def shiftZero():
	f = open('test_shift.txt','w')
	f.write("B[32] Sa[5] Cin C[32] \n")
	for i in [0, 1, 2, 3]:
		b = i
		for j in range(32):
			sa = str(j)
			temp = j
			cOut = b
			while temp > 0:
				cOut *= 2
				temp -= 1
			f.write(str(b) + ' ' + sa + ' 0 ' + str(cOut) + '\n')
	f.close()
