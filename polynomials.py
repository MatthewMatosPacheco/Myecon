"""NOT MY ALGORITHM!!! bELONGS TO DR fedor ISHAKOV"""
#qs is for coefficients( 5x^2+4x, 5 and 4 are coefficients)
def calc_polynomial(qs=[0,], x=0.0, algorithm='fast'):
#evaluates the polynomial given by coefficients qs at given x.
#First coefficient qs [0] is a constant, last coefficient is for the highest power
    if algorithm != 'fast':   #slower one
        res= 0.0
        for k in range(len(qs)):
            xpw= x**k # it takes x to the appropriate power
            res += qs[k]*xpw # results:it adds up coefficient with the power it calculated
        return print(res)
    else:#faster one
        res,xpw= qs[0],x #init result and power of x, (initialises to the power of x
        for i in range(1,len(qs)): #start with the second coefficient
            res += xpw * qs[i]
            xpw *=x# were accumulating the powers of x
        return print(res)
qs= [8,]*5  # the * 2 is the len of qs cuz qs = [], first k = 0
calc_polynomial(qs,4,'slow')
print(len(qs))
for k in range(len(qs)):
    print(k)
# in other words qs is the coeficient always the same in this scenario, multiplied by xpw and all summed up(k starts at 0
#alwasys same ( ax^y...)