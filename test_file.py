#!/usr/bin/env python3

from MatrixTools import *
getcontext().prec = 256 # float precision ( default 128 )

if __name__ == "__main__":

	Ma = Matrix([[1,2,3],[4,5,6],[7,8,9]])
	Mb = Matrix(csv_str="0,1,2\n3,4,5\n6,7,8")
	Mc = Matrix(csv_file="Mc.csv")
	Md = I(3)
	Mo = Matrix([[1,2,2],[2,-2,1],[2,1,-2]]) * Decimal(str(1/3))
	
	Mt = T(Ma)    #        ^___^
	Mm = Ma * Mb  #        |= =|
	Mk = Ma * 3   #         |_|             surcharger int pour 3 * Ma
	Mi = I(Mk)    #     . __|__  .
	Mtr = tr(Ma)  #     #_|\ / |_#      	tr(Ma) ~= Ma.trace()  
	Ms = Ma - Mb  #    ^    |               eg: self.trace_value
#	Mdv = Ma / Mb #    '-- /!\
	Mp = Ma ** 2  #      _/   \_
	Moo = Mo * T(Mo)
	Mr  = is_ort(Moo,2)
	Mid = is_id(Moo)				# means rounded to precision 2
	Midr = is_id(Moo,2)
	
	print("\n[matrix1 from list]\n")
	print(Ma)


	print("\n[matrix2 from csv string]\n")	
	print(Mb)	


	print("\n[matrix3 from csv file]\n")	
	print(Mc)		


	print("\n[identity matrix4]\n")
	print(Md)


	print("\n[matrix1 * matrix2]\n")
	print(Mm)

	print("\n[matrix1 * 3]\n")	
	print(Mk)

	print("\n[identity (matrix1 * 3)]\n")	
	print(Mi)

	print("\n[trace matrix1]\n")	
	print(Mtr)

	print("\n[matrix1 - matrix2]\n")	
	print(Ms)

	#print("\n[matrix * 1/3]\n")	
	#print(Mdiv)

	print("\n[matrix1 ** 2]\n")	
	print(Mp)

	print("\n[ matrix4 * 1/3 ]\n")	
	print(Mo)

	print("\n[ matrix5 = (matrix4 * 1/3) * Transpose(matrix4 * 1/3)]\n")	
	print(Moo)

	print("\n[is matrix5 orto ? (rounded)]\n")	
	print(Mr)

	print("\n[rounded 1.5248]\n")	
	print(round(1.5248,2))

	print("\n[is matrix5 identity ?]\n")	
	print(Mid)

	print("\n[is matrix5 identity ? (rounded)]\n")	
	print(Midr)

	
	
	
	
	
	
	
