#This program gives the solution(s) to a quadratic equaation
#of the form a*x**2+b*x+c=0
#Written by Alex Thierry

import math

def quadratic(a,b,c): #defining the quadratic function
    #solution
    discriminant = b*b - 4*a*c #discriminant
    p = round((-1*b)/(2*a),2) #Precision of 2dp
    if(discriminant == 0):
        #Repeated roots
        print('Repeated roots :',p)
    elif(discriminant > 0):
        #Real roots
        q = (math.sqrt(discriminant))/(2*a)
        root_1 = round(p + q,2) #Precision of 2dp
        root_2 = round(p - q,2)
        print('Real and distinct roots :',root_1,'or',root_2)
    else:
        #Complex roots
        q = round(math.sqrt(abs(discriminant))/(2*a),2)
        print('Complex roots : ',p,' + i',q,' or ',p,' - i',q,sep='')

if __name__ == '__main__':
    print('Enter the values of the coeficients')
    a = float(input('coeficient of x**2 : '))
    b = float(input('coeficient of x : '))
    c = float(input('constant : '))
    if a == 0:
        print('Equation is not a quadratic equation')
    else:
        quadratic(a,b,c)
    
