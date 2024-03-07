"""
Alexander Carrillo
EECS 210 Assignment 4
created 2/28/2024
last edit: 3/6/2024
All code is written by Alexander Carrillo

Inputs:

    Sets:
    oneToFour = [1,2,3,4]
    oneToThree = [1,2,3]
    zeroToThree = [0, 1, 2, 3]
    aToD = ['a','b','c','d']
    aToC = ['a','b','c']

    Relations:
    oneD = [[1,1],[4,4],[2,2],[3,3]]
    oneE = [['a','a'], ['c','c']]
    twoD = [[1,2],[4,4],[2,1],[3,3]]
    twoE = [[1,2],[3,3]]
    threeD = [['a','b'],['d','d'],['b','c'],['a','c']]
    threeE = [[1,1],[1,3],[2,2],[3,1],[3,2]]
    fourD = [[1,1],[2,2],[2,3]]
    fourE = [['a','a'],['b','b'],['c','c'],['b','c'],['c','b']]
    fiveD = [[1,1],[1,2],[2,2],[3,3],[4,1],[4,2],[4,4]]
    fiveE = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,2],[3,3]]
    
Inputs End.

Outputs:

1d)
R = [[1, 1], [4, 4], [2, 2], [3, 3]]
R is reflexive

1e)
R = [['a', 'a'], ['c', 'c']]
R is not reflexive
Reflexive closure for R:
R* = [['a', 'a'], ['c', 'c'], '[d,d]', '[b,b]']

2d)
R = [[1, 2], [4, 4], [2, 1], [3, 3]]
R is Symmetric

2e)
R = [[1, 2], [3, 3]]
R is not Symmetric
Symmetric closure for R:
R* = [[1, 2], [3, 3], [2, 1]]

3d)
R = [['a', 'b'], ['d', 'd'], ['b', 'c'], ['a', 'c']]
R is Transitive

3e)
R = [[1, 1], [1, 3], [2, 2], [3, 1], [3, 2]]
R is not Transitive
Transitive closure for R:
R* = [[1, 1], [1, 3], [2, 2], [3, 1], [3, 2], [1, 2], [3, 3]]

4d)
R = [[1, 1], [2, 2], [2, 3]]
relation is not an equivalice relation

Pairs missing for reflexivity: [3,3]
Pairs missing for symmetry: [3, 2]


4e)
R = [['a', 'a'], ['b', 'b'], ['c', 'c'], ['b', 'c'], ['c', 'b']]
relation is an equivalice relation

5d)
R = [[1, 1], [1, 2], [2, 2], [3, 3], [4, 1], [4, 2], [4, 4]]
relation is a poset

5e)
R = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 2], [3, 3]]
relation is not a poset

relation is not antisymmetric
Pair preventing antisymmetry: [1, 0][2, 0][0, 1][0, 2]
relation is not transitive
Pairs missing for transitivity: [2, 1][2, 3]

Ourputs End.
"""
#to be 100% honest I CAN NOT remember why I made this a set
#oh wait its because of repeats, thats why
def one(relation, theset):#reflexive
    missing = set() #set instead of list to prevent repeats 
    for i in theset:
        for j in relation:
            if [i,i] in relation:#checks to see if each pair that can be reflexive is in the set
                pass
            else:#if it isn't it adds it to missing that we use later after we call each function
                missing.add(f'[{i},{i}]')
    if len(missing) >= 1:
        return False, missing
    return True

def two(relation, theset):#symmetric
    missing = []
    for i in relation:
        if [i[1],i[0]] in relation:#checks to see if the reflected value is there
            pass
        else:#if it isn't it adds it to missing that we use later after we call each function
            missing.append([i[1],i[0]])
    if len(missing) >= 1:
        return False, missing
    return True

def three(relation, theset):#transitive
    missing = []
    for i in relation:
        for j in relation:
            if i[1] == j[0]:
                if [i[0], j[1]] not in relation:#checks to see if the value for transitivity is there
                    missing.append([i[0],j[1]])
    if len(missing) >= 1:#if it isn't it adds it to missing that we use later after we call each function
        return False, missing
    return True


def four(relation, theset):#equivalice relation, needs reflexive, symmetric, and transitive == True
    if one(relation, theset) == True and two(relation, theset) == True and three(relation, theset) == True:
        print('relation is an equivalice relation')
        return True
    else:#going through each function's missing list and printing those out and passing if it returned true
        print('relation is not an equivalice relation')
        try:#check for one()
            missing = one(relation,theset)[1]#each of these just take the missing list from the function and then iteratses throught the pairs in it
            print('\nPairs missing for reflexivity: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        try:#check for two()
            missing = two(relation,theset)[1]
            print('\nPairs missing for symmetry: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        try:#check for three()
            missing = three(relation,theset)[1]
            print('\nPairs missing for transitivity: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        print('\n')
        return False
        
#to make a new function or just wing it in this one...
def five(relation, theset):#poset, needs reflexive, transitive, and antisym == True
    if one(relation, theset) == True and antisym(relation, theset) == True and three(relation, theset) == True:
        print('relation is a poset')
        return True
    else:#same as four() but two() is swapped with antsym()
        print('relation is not a poset')
        try:#check for one()
            missing = one(relation,theset)[1]#each of these just take the missing list from the function and then iteratses throught the pairs in it
            print('\nrealation is not reflexive')
            print('Pairs missing for reflexivity: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        try:#check for antisym
            missing = antisym(relation,theset)[1]
            print('\nrelation is not antisymmetric')
            print('Pair preventing antisymmetry: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        try:#check for three()
            missing = three(relation,theset)[1]
            print('\nrelation is not transitive')
            print('Pairs missing for transitivity: ', end = '')
            for i in missing:
                print(i, end = '')
        except:
            pass
        print('\n')
        return False
    
def antisym(relation, theset):#antisymmetric function for five()
    notmissing = []
    for i in relation:#need to prevent it seeing reflexive pairs as antitsym
        if [i[1],i[0]] not in relation or i[1] == i[0]:#easy, added the LHS of the or to pass on reflexive pairs
            pass
        else:
            notmissing.append([i[1],i[0]])
    if len(notmissing) >= 1:
        return False, notmissing
    return True#pretty much the exact same as two() with changes to the if statement
    
    

def main():
    """sets"""
    oneToFour = [1,2,3,4]#the set for the 'theset' of the functions, used for output of 1d, 2d, 2e, and 5e
    oneToThree = [1,2,3]#set for 3e
    zeroToThree = [0, 1, 2, 3]#set for 5f
    aToD = ['a','b','c','d']#set for 1e, 3d,
    aToC = ['a','b','c']#set for 4e
    """sets end"""
    """relations"""
    #the name of each directly matches the problem for the assignment
        #i.e. oneD will be used in 1d)
    oneD = [[1,1],[4,4],[2,2],[3,3]]
    oneE = [['a','a'], ['c','c']]
    twoD = [[1,2],[4,4],[2,1],[3,3]]
    twoE = [[1,2],[3,3]]
    threeD = [['a','b'],['d','d'],['b','c'],['a','c']]
    threeE = [[1,1],[1,3],[2,2],[3,1],[3,2]]
    fourD = [[1,1],[2,2],[2,3]]
    fourE = [['a','a'],['b','b'],['c','c'],['b','c'],['c','b']]
    fiveD = [[1,1],[1,2],[2,2],[3,3],[4,1],[4,2],[4,4]]
    fiveE = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,2],[3,3]]
    """relations end"""
    """outputs"""
    #1d)
    print(f'1d)\nR = {oneD}')
    if one(oneD, oneToFour) == True:
        print('R is reflexive')
    else:
        print('R is not reflexive')
        closed = oneD
        for i in one(oneD, oneToFour)[1]:
            closed.append(i)
        print(f'Reflexive closure for R:\nR* = {closed}')
    
    #1e)
    print(f'\n1e)\nR = {oneE}')
    if one(oneE, aToD) == True:
        print('R is reflexive')
    else:
        print('R is not reflexive')
        closed = oneE
        for i in one(oneE, aToD)[1]:
            closed.append(i)
        print(f'Reflexive closure for R:\nR* = {closed}')
    #2d)
    print(f'\n2d)\nR = {twoD}')
    if two(twoD, oneToFour) == True:
        print('R is Symmetric')
    else:
        print('R is not Symmetric')
        closed = twoD
        for i in two(twoD, oneToFour)[1]:
            closed.append(i)
        print(f'Symmetric closure for R:\nR* = {closed}')
    #2e)
    print(f'\n2e)\nR = {twoE}')
    if two(twoE, oneToFour) == True:
        print('R is Symmetric')
    else:
        print('R is not Symmetric')
        closed = twoE
        for i in two(twoE, oneToFour)[1]:
            closed.append(i)
        print(f'Symmetric closure for R:\nR* = {closed}')
    #3d)
    print(f'\n3d)\nR = {threeD}')
    if three(threeD, aToD) == True:
        print('R is Transitive')
    else:
        print('R is not Transitive')
        closed = threeD
        for i in three(threeD, aToD)[1]:
            closed.append(i)
        print(f'Transitive closure for R:\nR* = {closed}')
    #3e)
    print(f'\n3e)\nR = {threeE}')
    if three(threeE, oneToThree) == True:
        print('R is Transitive')
    else:
        print('R is not Transitive')
        closed = threeE
        for i in three(threeE, oneToThree)[1]:
            closed.append(i)
        print(f'Transitive closure for R:\nR* = {closed}')
    #4d)
    print(f'\n4d)\nR = {fourD}')
    four(fourD, oneToThree)
    #4e)
    print(f'\n4e)\nR = {fourE}')
    four(fourE, aToC)
    #5d)
    print(f'\n5d)\nR = {fiveD}')
    five(fiveD, oneToFour)
    #5e)
    print(f'\n5e)\nR = {fiveE}')
    five(fiveE, zeroToThree)
    """outputs end"""
main()
