"""
Alexander Carrillo
EECS 210 Assignment 3
created 2/18/2024
last edit: 2/22/2024
All code is written by Alexander Carrillo
inputs: there are no inputs, all the functions take nothing and there is no user input
outputs of functions:
a1(): [(3, 3), (1, 2), (2, 2), (1, 1), (1, 3), (1, 4)]
b1(): [(1, 1)]
c1(): [(3, 3), (2, 2)]
d1(): [(1, 2), (1, 3), (1, 4)]

prob2(): [[3, 1], [3, 4], [3, 3], [4, 1], [4, 4]]

prob3(): [[1, 1], [1, 4], [2, 1], [2, 4], [3, 1], [3, 4]]

a4():[[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10]]
b4():False
c4():True
d4():False
e4():False

Sample output:
1.
a) Union of R1 and R2: [(3, 3), (1, 2), (2, 2), (1, 1), (1, 3), (1, 4)]
b) Intersection of R1 and R2: [(1, 1)]
c) Difference of R2 from R1: [(3, 3), (2, 2)]
d) Difference of R1 from R2: [(1, 2), (1, 3), (1, 4)]

2. R o S
[[3, 1], [3, 4], [3, 3], [4, 1], [4, 4]]

3. R^2
[[1, 1], [1, 4], [2, 1], [2, 4], [3, 1], [3, 4]]

4.
a) R as a set of ordered pairs: [[-10, 10], [-9, 9], [-8, 8], [-7, 7], [-6, 6], [-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9], [10, -10]]
b) Is R reflexive?: False
c) Is R symmetric?: True
d) Is R antisymmetric?: False
e) Is R transitive?: False
"""
"""Problem 1 functions"""
#Relations list for R1 and R2
R1 = [tuple([1,1]),tuple([2,2]),tuple([3,3])]#lists dont work for these operators so I made the tuples
R2 = [tuple([1,1]),tuple([1,2]),tuple([1,3]),tuple([1,4])]
def a1():#union of R1 and R2
    union = list(set(R1) | set(R2))
    return union
        
def b1():#intersetion of R1 and R2
    intsec = list(set(R1) & set(R2))
    return intsec

def c1():#R1 - R2
    onediff = list(set(R1) - set(R2))
    return onediff

def d1():#R2 - R1
    twodiff = list(set(R2) - set(R1))
    return twodiff
"""Problem 1 functions end"""

"""Problem 2 functions"""
#Relations lists for R and S
A = [1,2,3]
B = [1,2,3,4]
C = [0,1,2]
R = [[1,1], [1,4], [2,3], [3,1], [3,4]]#Mostly using R and S
S = [[1,0], [2,0], [3,1], [3,2], [4,1]]
def prob2():#R o S
    RoS = []
    for i in S:#going through S and then R
        for j in R:
            if i[1] == j[0]:#if the second value in i for S is the same as the first value of j in R we take the head from R and the Tail from S and put them in an ordered pair
                RoS.append([i[0],j[1]])#then put it into our composite list RoS
    return RoS#then return RoS
"""Problem 2 functions end"""

"""Problem 3 functions"""
def prob3():#R o R
    RoR = []
    for i in R:#just using the R list from the prob2, and replaced any reference to S to R, RoS is now RoR
        for j in R:
            if i[1] == j[0]:
                RoR.append([i[0],j[1]])
    return RoR
"""Problem 3 functions end"""

"""Problem 4 functions"""
def a4():#creates a set by iterating through the range -10-10 twice and then seeing which pairs sums equal 0, and then returns that list of pairs
    setR = []
    for i in range(-10,11):
        for j in range(-10,11):
            if i + j == 0:
                setR.append([i,j])
    return setR

def b4():#takes list from a4 and checks if the numbers in the ordered pairs are the same
    for i in a4():
        if i[0] != i[1]:
            return False#for the given example will always return false
    return True

def c4():#takes list from a4 and checks if the list given is symmetric 
    yep = 0
    for i in a4():
        for j in a4():
            if j[0] == i[1] and j[1] == i[0]:#looks to see if there is a pair for i that it is symmetric to in j, then adds one to yep
                yep += 1
    if yep == len(a4()):#checks if each pair was symmetric
        return True#for this example it will always return True
    else:
        return False
    
                
    
def d4():#takes list from a4 and checks if the list given is antisymmetric 
    yep = 0
    for i in a4():
        for j in a4():
            if j[0] != i[1] or j[1] != i[0]:#opposite of c4
                yep += 1
    if yep == len(a4()):#checks if each pair was antisymmetric
        return True
    else:
        return False#for this example it will always return False
    
def e4():#iterates through two coppies of a4 and finds wether a4 is transitive or not 
    for i in a4():
        for j in a4():
            if i[1] == j[0]:#check to see if we have the oprtunity for transitive-ness
                if (i[0], j[1]) not in a4():#check a4 to see if we have a pair that would make it transitive, if not we return False
                    return False#for this example it will always return false
    return True
"""Problem 4 functions end"""



def main():
    print('1.')
    print(f'a) Union of R1 and R2: {a1()}')
    print(f'b) Intersection of R1 and R2: {b1()}')
    print(f'c) Difference of R2 from R1: {c1()}')
    print(f'd) Difference of R1 from R2: {d1()}\n')

    print('2. R o S')
    print(prob2())

    print('\n3. R^2')
    print(prob3())

    print('\n4.')
    print(f'a) R as a set of ordered pairs: {a4()}')
    print(f'b) Is R reflexive?: {b4()}')
    print(f'c) Is R symmetric?: {c4()}')
    print(f'd) Is R antisymmetric?: {d4()}')
    print(f'e) Is R transitive?: {e4()}')
    
    
    
    
main()
