from copy import deepcopy
from decimal import *
getcontext().prec = 128

def Test(matrix):
	if isinstance(matrix,Matrix):
		return True
	return False

def T(matrix):
	if not isinstance(matrix,Matrix) :
		matrix = Matrix(matrix)
	return matrix.transpose()

def tr(matrix):
	if not isinstance(matrix,Matrix):
		matrix = Matrix(matrix)
	return matrix.trace()

def is_ort(matrix,rounded=False):
	if not isinstance(matrix,Matrix):
		matrix = Matrix(matrix)
	return matrix.is_ort(rounded)

def is_id(matrix,rounded=False):
	if not isinstance(matrix,Matrix):
		matrix = Matrix(matrix)
	return matrix.is_id(rounded)

def I(matrix):
	if type(matrix) is int :
		return Matrix([[1 if i==j else 0 for j in range(matrix)] for i in range(matrix)])
	if not isinstance(matrix,Matrix) :
		matrix = Matrix(matrix)
	return matrix.unite()

class ExceptionMatrice(Exception):
	def __init__(self,exception):
		self.exception = str(exception)
	def __str__(self):
		return self.exception

class Matrix():
	
	def __init__(self,matrix=None,csv_str=None,csv_file=False,unpecise=False,rounded=False):
		self.csv_file = csv_file
		self.csv_str = csv_str
		self.matrix = deepcopy(matrix)
		self.trace_value = None
		self.orth_value = None
		self.unpecise = unpecise
		self.rounded = rounded
		self.setM()
		
		
	def __add__(self,b):
		if not isinstance(b,Matrix):
			raise ExceptionMatrice("The action you try to achieve is not possible at the moment ...")
		if self.nb_lignes != b.nb_lignes or self.nb_cols != b.nb_cols:
			raise ExceptionMatrice("The matrixs you're using are not compatible")
		else:
			return Matrix([[self.matrix[i][j] + b.matrix[i][j] for j in self.nb_cols] for i in self.nb_lignes])

	def __mul__(self,b):
		if isinstance(b,Decimal) \
		or type(b) is int \
		or type(b) is float:
			return self.mprod_scal(Decimal(str(b)))
		if isinstance(b,Matrix) :
			return self.mprod(b)
		
	def __sub__(self,b):
		if not isinstance(b,Matrix):
			raise ExceptionMatrice("The action you try to achieve is not possible at the moment ...")
		if self.nb_lignes != b.nb_lignes or self.nb_cols != b.nb_cols:
			raise ExceptionMatrice("The matrixs you're using are not compatible")
		else:
			return Matrix([[self.matrix[i][j] - b.matrix[i][j] for j in self.nb_cols] for i in self.nb_lignes])
		
	def __neg__(self):
		return self.mprod_scal(-1)

	def __pow__(self,n):
		if n == 0: return self.unite()
		pA = Matrix(self.matrix)
		k = n - 1
		while k > 0:
			if k%2 == 0:
				pA = pA * pA
				k /= 2 
			else:
				pA = self * pA
				k -= 1
		return pA

	def __div__(self,b):
		if isinstance(b,Decimal) \
		or type(b) is int \
		or type(b) is float:
			return self.mdiv_scal(Decimal(str(b)))
		if isinstance(b,Matrix):
			return self.mdiv(b)	
		
	def __str__(self):
		result = ""
		for lignes in self.matrix:
			for elem in lignes:
				result += str(float(elem)) + ' '
			result += "\n"
		return result[:-1]
	'''
	def __index__(self,x=None,y=None):
		if str(type(x)) == "<class 'int'>":
			if str(type(y)) == "<class 'int'>":
				return self.matrix[x][y]
			return self.matrix[x]
		return self.matrix
	'''	
	
	def mdiv(self,b):
		if not isinstance(b,Matrix) \
		or self.nb_cols != b.nb_lignes:
			raise ExceptionMatrice("The matrixs you're using are not compatible")
		tb = T(b)
		C = [[0 for p in b.nb_cols] for p in self.nb_lignes]
		for i in self.nb_lignes:
			Ai, Ci = self.matrix[i], C[i]
			for j in self.nb_cols:
				tbj = tb.matrix[j]
				for k in tb.nb_lignes:
					Ci[j] += Ai[k] / tbj[k]
		return Matrix(C)
		
	
	def mprod(self,b):
		if not isinstance(b,Matrix) \
		or self.nb_cols != b.nb_lignes:
			raise ExceptionMatrice("The matrixs you're using are not compatible")
		tb = T(b)
		C = [[0 for p in b.nb_cols] for p in self.nb_lignes]
		for i in self.nb_lignes:
			Ai, Ci = self.matrix[i], C[i]
			for j in self.nb_cols:
				tbj = tb.matrix[j]
				for k in tb.nb_lignes:
					Ci[j] += Ai[k]*tbj[k]
		return Matrix(C)
		
	def unite(self):
		return Matrix([[1 if i==j else 0 for j in self.nb_lignes] for i in self.nb_lignes])
		
	def transpose(self):
		return Matrix([[ self.matrix[i][j] for i in self.nb_lignes] for j in self.nb_cols])

	def trace(self):
		if self.nb_lignes != self.nb_cols:
			raise ExceptionMatrice("Not suitable matrix")
		t = 0
		for i in self.nb_lignes:
			t += self.matrix[i][i]
		self.trace_value = t
		return t

	def is_ort(self,rounded=False):
		if self.nb_lignes != self.nb_cols:
			raise ExceptionMatrice("Not suitable matrix")
		if rounded != False:
			matrix = [[ round(self.matrix[i][j],rounded) for j in self.nb_cols] for i in self.nb_lignes]
		else:
			matrix = deepcopy(self.matrix)
		for j in self.nb_cols:
			N = 0
			for i in self.nb_lignes:
				N += (matrix[i][j])**2
			if N != 1 :
				self.orth_value = False
				return False # each cols norm should be eq. to 1
			for k in range(j+1,len(self.nb_cols)):
				P = 0
				for i in self.nb_lignes:
					P += matrix[i][j] *  matrix[i][k]
				if P != 0 :
					self.orth_value = False
					return False # each scalar prod. should be eq. to 0
		self.orth_value = True
		return True	
		
	def mdiv_scal(self,k):
		return Matrix([[k / self.matrix[i][j] for j in self.nb_cols] for i in self.nb_lignes])

	def mprod_scal(self,k):
		return Matrix([[k * self.matrix[i][j] for j in self.nb_cols] for i in self.nb_lignes])

	def setM(self):
		if type(self.matrix) is not list:
			if type(self.csv_str) is str:
				self.matrix = [ elem.split(',') for elem in str(self.csv_str).split("\n") ]
			elif type(self.csv_file) is str :
				try:
					with open(self.csv_file,'r') as f:
						self.matrix = [ligne.split(',') for ligne in f]
				except:
					raise ExceptionMatrice("Can't open csv file")
			else:
				raise ExceptionMatrice("Nothing to reset")
		if self.matrix == [] or type(self.matrix[0]) is not list or self.matrix[0] == []:
			raise ExceptionMatrice("Empty Matrix")
		if self.rounded != False:
			self.matrix = [ [round(float(elem),int(self.rounded)) for elem in row] for row in self.matrix ]
		if type(self.matrix[0][0]) is not Decimal \
		and self.unpecise == False:
			self.matrix = [ [Decimal(str(elem)) for elem in row] for row in self.matrix ]
		self.nb_lignes = self.lignes()
		self.nb_cols = self.cols()
		if self.rounded == False \
		and self.unpecise == True:
			for i in self.nb_lignes:
				for j in self.cols:
					if type(self.matrix[i][j]) is Decimal:
						self.matrix[i][j] = float(self.matrix[i][j])
					if type(self.matrix[i][j]) is not int \
					or type(self.matrix[i][j]) is not float \
					or type(self.matrix[i][j]) is not str :
						raise ExceptionMatrice("Not valide values")
	
	def lignes(self):
		return range(len(self.matrix))

	def cols(self):
		return range(len(self.matrix[0]))		
		
	def is_id(self,rounded=False):
		if self.nb_lignes != self.nb_cols:
			raise ExceptionMatrice("Not suitable matrix")
		for i in self.nb_lignes:
			for j in self.nb_cols:
				if i == j:
					test = 1
				else:
					test = 0
				if rounded != False:
					if round(float(self.matrix[i][j]),rounded) != test:
						return False
				else:
					if float(self.matrix[i][j]) != test:
						return False
		return True
		
