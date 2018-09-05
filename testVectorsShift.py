def shiftZero():
	f = open('test_shift.txt','w')
	f.write("B[32] Sa[5] Cin C[32] \n")
	for i in [0, 1, 2, 3]:
		b = bin(i)[2:].rjust(32, '0')
		for j in range(32):
			sa = str(j)
			cOut = b[j:].ljust(32, '0')

			f.write(str(b) + ' ' + sa + ' 0 ' + str(cOut) + '\n')
	f.close()
