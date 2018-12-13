from .context import numerical_methods
from numerical_methods.equation_solution import (Symbol, contains_singularity,
                                                  intvl_contains_root)

import unittest


class TestEquationSolution(unittest.TestCase):


# contains_singularity
    def test_contains_singularity_eq_with_no_singularities(self):
        x = Symbol('x')
        f = -x -1 + x ** 3 
        assert contains_singularity(f,x,-1E10,1E10) == False

    def test_contains_singularity_eq_with_singularities_in_interval(self):
        x = Symbol('x')
        f = 1 /x  
        assert contains_singularity(f,x,-1,1) == True

    def test_contains_singularity_eq_with_singularities_outside_interval(self):
        x = Symbol('x')
        f = 1 /x  
        assert contains_singularity(f,x,-1E10,-1E-10) == False    
        assert contains_singularity(f,x,1E-10,1E10) == False    

# intvl_contains_root
    def test_intvl_contains_root_eq_with_root_in_interval(self):
        x = Symbol('x')
        f = -x -1 + x ** 3 
        assert intvl_contains_root(f,x,-1E10,1) == False

    def test_intvl_contains_root_eq_with_root_outside_interval(self):
        x = Symbol('x')
        f = -x -1 + x ** 3 
        assert intvl_contains_root(f,x,0,4) == True

if __name__ == '__main__':
    unittest.main()

