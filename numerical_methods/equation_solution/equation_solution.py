from sympy import *

def contains_singularity(f,var,a,b):
    contains = False
   
    singular_points = list(singularities(f,var))
    for singularity in singular_points:
        if singularity >= a and singularity <= b:
            contains = True
    
    return contains

def is_applyable(f, var, a, b):
    applyable = True
    f1 = f.subs(var, a)
    f2 = f.subs(var, b)

    if(f1 * f2 > 0):
        applyable = False
    
    else:
        
        df = diff(f, var)
        df1 = df.subs(x,a)
        df2 = df.subs(x,b)
        if(df1 * df2 < 0):
            applyable = False                 
     
        else:
            if contains_singularity(f,var,a,b): 
                applyable = False
   
    return applyable


x = Symbol('x')

a = -2 
b = 2
tolerance = 0.00001

fx = x ** 2 + 3 * x 
print(is_applyable(fx,x,a,b))
