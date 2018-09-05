def shiftZero():
	f = open('test_shift.txt','w')
	f.write("B[32] Sa[5] Cin C[32] \n")
	f.write("#testing all shifts on various numbers, including the smallest and biggest possible number \n")
	for i in [0, 1, 2, 3, 4, 8, 100, 3524325, pow(2, 31), pow(2, 32) - 1]:
		b = bin(i)[2:].rjust(32, '0')
		for j in range(32):
			sa = str(j)
			cOut = b[j:].ljust(32, '0')

			f.write(b + ' ' + sa + ' 0 ' + cOut + '\n')
	f.close()
