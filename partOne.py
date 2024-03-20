"""
Alexander Carrillo
EECS 210 Assignment 4
created 3/12/2024
last edit: 3/20/2024
All code is written by Alexander Carrillo

Inputs:
#a
    A  = {'a','b','c','d'}
    B = {'v','w','x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','w')]

#b
    A  = {'a','b','c','d'}
    B = {'x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','z')]

#c
    A  = {'a','b','c','d'}
    B = {'w','x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','w')]

#d
    A  = {'a','b','c','d'}
    B = {1,2,3,4,5}
    f = [('a',4),('b',5),('c',1),('d',3)]

#e
    A  = {'a','b','c'}
    B = {1,2,3,4}
    f = [('a',3),('b',4),('c',1)]

#f
    A  = ['a','b','c','d']
    B = {1,2,3}
    f = [('a',2),('b',1),('c',3),('d',2)]

#g
    A  = {'a','b','c','d'}
    B = {1,2,3,4}
    f = [('a',2),('b',1),('c',3),('d',2)]

#h
    A  = ['a','b','c','d']
    B = {1,2,3,4}
    f = [('a',2),('b',1),('c',2),('d',3)]

#i
    A  = {'a','b','c'}
    B = {1,2,3,4}
    f = [('a',2),('b',1),('a',4),('c',3)]

Outputs:
a
The relation is a function.
The function is injective.

b
The relation is a function.
The function is surjective.

c
The relation is a function.
The function is injective.
The function is surjective.
The function is bijective.
The inverse function is:
['z', 'a'] ['y', 'b'] ['x', 'c'] ['w', 'd']

d
The relation is a function.
The function is injective.

e
The relation is a function.
The function is injective.

f
The relation is a function.
The function is surjective.

g
The relation is a function.

h
The relation is a function.

i
The relation is not a function.
"""
def is_function(A, B, f):#checks if each element in the domain maps to exactly one element in the codomain
    domain_elements = set()
    for i in f:
        domain_elements.add(i[0])
    if not all(element in A for element in domain_elements):#checks if all elements in the domain are from set A
        return False
    if not all(i[1] in B for i in f):#checks if all elements in the codomain are from set B
        return False
    domain_mapping = {}
    for i in f:#checks if no two elements in the domain map to the same element in the codomain
        if i[0] in domain_mapping:
            return False
        domain_mapping[i[0]] = i[1]
    return True
    
def is_injective(f):#checks if no two elements in the domain map to the same element in the codomain
    codomain_elements = set()
    for i in f:
        codomain_elements.add(i[1])
    return len(codomain_elements) == len(f)

def is_surjective(A, B, f):#checks to see if every element in the codomain is being used by the domain in the function
    for i in B:
        found = False
        for j in A:
            if (j, i) in f:
                found = True
                break
        if not found:
            return False
    return True

def is_bijective(A,B,f):#checks to see if the relation is a function, injective, and surjective for it to be bijective
    return is_function(A,B,f) and is_injective(f) and is_surjective(A,B,f)

def inverse_function(A,B,f):#checks bijection, then returns the inverse of the relation
    if not is_bijective(A,B,f):#bijection check
        return None
    inverse = []
    for i in f:#inversion
        inverse.append([i[1],i[0]])
    return inverse #returns inversed relation

def main():
    """sample inputs"""
    """
    #a
    A  = {'a','b','c','d'}
    B = {'v','w','x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','w')]
    """
    """ 
    #b
    A  = {'a','b','c','d'}
    B = {'x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','z')]
    """
    """
    #c
    A  = {'a','b','c','d'}
    B = {'w','x','y','z'}
    f = [('a','z'),('b','y'),('c','x'),('d','w')]
    """
    """
    #d
    A  = {'a','b','c','d'}
    B = {1,2,3,4,5}
    f = [('a',4),('b',5),('c',1),('d',3)]
    """
    """
    #e
    A  = {'a','b','c'}
    B = {1,2,3,4}
    f = [('a',3),('b',4),('c',1)]
    """
    """
    #f
    A  = ['a','b','c','d']
    B = {1,2,3}
    f = [('a',2),('b',1),('c',3),('d',2)]
    """
    """
    #g
    A  = {'a','b','c','d'}
    B = {1,2,3,4}
    f = [('a',2),('b',1),('c',3),('d',2)]
    """
    """
    #h
    A  = ['a','b','c','d']
    B = {1,2,3,4}
    f = [('a',2),('b',1),('c',2),('d',3)]
    """
    
    #i
    A  = {'a','b','c'}
    B = {1,2,3,4}
    f = [('a',2),('b',1),('a',4),('c',3)]
    
    
    """output"""
    print('i')#print for the target problem
    if is_function(A,B,f):#function check
        print("The relation is a function.")
        if is_injective(f):#injecive check
            print("The function is injective.")
        if is_surjective(A,B,f):#surjective check
            print("The function is surjective.")
        if is_bijective(A,B,f):#bijective check
            print("The function is bijective.")
            inverse = inverse_function(A,B,f)#gets inverse
            print("The inverse function is:")
            for i in inverse:
                print(i, end = ' ')
    else:#not a function
        print("The relation is not a function.")

main()
