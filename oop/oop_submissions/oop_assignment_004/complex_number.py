class ComplexNumber:
    def __init__(self,real_part = 0,imaginary_part = 0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
        if type(self.real_part)==str and type(self.imaginary_part)==str:
            raise ValueError('Invalid value for real and imaginary part')
            
        if type(self.real_part)==str:
            raise ValueError('Invalid value for real part')
            
        if type(self.imaginary_part)==str:
            raise ValueError('Invalid value for imaginary part')
            
    def __str__(self):
        if self.imaginary_part>=0:
            return '{}+{}i'.format(self.real_part,self.imaginary_part)
        if self.imaginary_part<0:
            return '{}{}i'.format(self.real_part,self.imaginary_part)

    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
    
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,
        self.imaginary_part+other.imaginary_part)  
        
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,
        self.imaginary_part-other.imaginary_part)   
    
    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
        self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
        
    
    def __truediv__(self, other):
        sr, si, Or, Oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part
        r = float(Or**2 + Oi**2)
        return ComplexNumber((sr*Or+si*Oi)/r, (si*Or-sr*Oi)/r)
        
        
        
    def __abs__(self):
        return round(((self.real_part**2 + self.imaginary_part**2)**0.5),3)
    
    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
