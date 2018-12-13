from sympy import Symbol, singularities, diff

def contains_singularity(f,var,a,b):
    contains = False
   
    singular_points = list(singularities(f,var))
    for singularity in singular_points:
        if singularity >= a and singularity <= b:
            contains = True
    
    return contains

def df_sign_constant(f,var,a,b):
    sign_constant = True
    df = diff(f, var)
    df1 = df.subs(var,a)
    df2 = df.subs(var,b)

    if(df1 * df2 < 0): 
        sign_constant = False 

    return sign_constant

def intvl_contains_root(f,var,a,b):
    contains_root = True 
    f1 = f.subs(var, a)
    f2 = f.subs(var, b)

    if(f1 * f2 > 0):
        contains_root = False
    
    return contains_root

def is_applyable(f,var,a,b):
    applyable = True

    if not intvl_contains_root(f,var,a,b): 
        applyable = False
    
    else:
        
        if not df_sign_constant(f,var,a,b):            
            applyable = False                 
     
        else:
            if contains_singularity(f,var,a,b): 
                applyable = False
   
    return applyable