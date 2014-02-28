from MatrixTools import *
getcontext().prec = 256 # float precision ( default 128 )

if __name__ == "__main__":

	Ma = Matrix([[1,2,3],[4,5,6],[7,8,9]])
	Mb = Matrix(csv_str="0,1,2\n3,4,5\n6,7,8")
	Mc = Matrix(csv_file="Mc.csv")
	Md = I(3)
	Mo = Matrix([[1,2,2],[2,-2,1],[2,1,-2]]) * Decimal(str(1/3))
	
	Mt = T(Ma)    #        ^___^
	Mm = Ma * Mb  # 	   |= =|
	Mk = Ma * 3   #   	    |_|             surcharger int pour 3 * Ma
	Mi = I(Mk)    #     . __|__  .
	Mtr = tr(Ma)  #     #_|\ / |_#      	tr(Ma) ~= Ma.trace()  
	Ms = Ma - Mb  #    ^    |               eg: self.trace_value
#	Mdv = Ma / Mb #    '-- /!\
	Mp = Ma ** 2  #      _/   \_
	Moo = Mo * T(Mo)
	Mr  = is_ort(Moo,2)
	Mid = is_id(Moo)				# means rounded to précision 2
	Midr = is_id(Moo,2)
	
	print(Ma)
	print("------")
	
	print(Mb)	
	print("------")
	
	print(Mc)		
	print("------")

	print(Md)
	print("------")

	print(Mm)
	print("------")
	
	print(Mk)
	print("------")
	
	print(Mi)
	print("------")
	
	print(Mtr)
	print("------")
	
	print(Ms)
	print("------")
	
	#print(Mdiv)
	#print("------")
	
	print(Mp)
	print("------")
	
	print(Moo)
	print("------")
	
	print(Mr)
	print("------")
	
	print(round(1.5248,2))
	print("------")
	
	print(Mid)
	print("------")
	
	print(Midr)
	print("------")
	
	
	
	
	
	
	
