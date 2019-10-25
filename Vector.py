class Vector(list):

    '''A list-based Vector class.'''    

    def __add__(self, other):
        try:
            return Vector(map(lambda x, y: x + y, self, other))
        except TypeError: #to do scalar addition
            return Vector(map(lambda x: x + other, self))

    def __neg__(self):
        return Vector(map(lambda x: - x, self))

    def __sub__(self, other):
        #subtraction operation of Vector
        try:
            return Vector(map(lambda x, y: x - y, self, other))
        except TypeError: #to do scalar subtraction
            return Vector(map(lambda x: x - other, self))
    
    def __mul__(self, other):
        #inner product of Vector
        try:
            return Vector(map(lambda x, y: x * y, self, other))
        except TypeError: #to do scalar multiplication
            return Vector(map(lambda x: x * other, self))
    
    def __div__(self, other):
        #division operation of Vector
        try:
            return Vector(map(lambda x, y: x / y, self, other))
        except TypeError: #to do scalar division
            return Vector(map(lambda x: x / other, self))
        
    def __radd__(self, other):      
        try:
            return Vector(map(lambda x, y: x + y, self, other))
        except TypeError: #to do scalar addtion from RHS
            return Vector(map(lambda x: other + x, self))

    def __rsub__(self, other):
        #subtraction operation of Vector
        try: 
            return Vector(map(lambda x, y: x - y, self, other))
        except TypeError: #to do scalar subtraction from RHS
            return Vector(map(lambda x: other - x, self))
    
    def __rmul__(self, other):
        #inner product of Vector 
        try:
            return Vector(map(lambda x, y: x * y, self, other))
        except TypeError: #to do scalar multiplication from RHS
            return Vector(map(lambda x: other * x, self))
    
    def __rdiv__(self, other):
        #division operation of Vector
        try:
            return Vector(map(lambda x, y: x / y, self, other))
        except TypeError: #to do scalar division from RHS
            return Vector(map(lambda x: other / x , self))
'''
if __name__ == "__main__":
	x = Vector([1,2,2])
	y = Vector([1,2,4])

	print x + y
'''
