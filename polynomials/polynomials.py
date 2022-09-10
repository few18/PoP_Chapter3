from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            other.coefficients = tuple([-1*c for c in other.coefficients])
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        return self - other

    
    def __mul__(self, other):

        if isinstance(other, Number):
            coefs = tuple([other*c for c in self.coefficients])
            return Polynomial(coefs)

        elif isinstance(other, Polynomial):
            # Get degree of both polynomials
            self_degree = self.degree()
            other_degree = other.degree()

            # Calulate degree of resulting polynomial
            result_degree = self_degree + other_degree

            # Make list of required lenght filled with zeros
            coefs = []
            for i in range(result_degree + 1):
                coefs.append(0)
            
            # Start a grid multiplying the coefficients
            for index1, coef1 in enumerate(self.coefficients):
                for index2, coef2 in enumerate(other.coefficients):

                    coefs[index1 + index2] += coef1 * coef2

            return Polynomial(tuple(coefs))

        else:
            return NotImplemented

    
    def __rmul__(self, other):
        return self * other

    def __pow__(self, exponent):
        
        exponentiated = self.__mul__(1)

        # Repeatedly use __mul__() to exponentiate
        for i in range(exponent - 1):

            exponentiated = exponentiated.__mul__(self)
        
        return exponentiated

    
    def __call__(self, x):

        if isinstance(x, Number):

            value = 0

            for power, coef in enumerate(self.coefficients):

                value += coef * (pow(x, power))

            return value
        
        else:
            return NotImplemented

    

    
