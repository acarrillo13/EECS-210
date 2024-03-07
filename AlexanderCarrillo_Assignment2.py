"""
Alexander Carrillo
ID: 3052107
EECS 210 Assignment 2
file created: 1/26/2024
Program that returns truth values for a number of assertations using both singular and nested quantifiers
"""
###ALL CODE IS WRITTEN BY ME###
"""First problem functions"""
def a1():#∃xP(x) | P(x) = x < 2
    for x in range(0,11):
        if x < 2:
            return True, x#truth value of function, number where it is proven
    return False, 'for all of 0-10'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
def b1():#∀xP(x) | P(x) = x < 2 
    for x in range(0,11):
        if x > 2:
            return False, x #truth value of function, number where it is proven
    return True, 'for all of 0-10'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
def c1():#∃x(P(x) ∨ Q(x))| P(x) = x < 2 | Q(x) = x > 7
    for x in range(0,11):
        if x < 2 or x > 7:
            return True, x#truth value of function, number where it is proven
    return False, 'for all of 0-10'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
def d1():#∀x(P(x) ∨ Q(x)) | P(x) = x < 2 |  Q(x) = x > 7
    count = 0
    for x in range(0,11):
        if x < 2 or x > 7:
            count += 1
    if count == 10:
        return True, x#truth value of function, number where it is proven
    else:
        return False, 'for all of 0-10'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
    
#what are the demorgans asking for??? do they want me to prove that ∃x(P(x)) == -(∀x(-P(x))) or just to print the value of one of those functons?????
def e1():#Demorgan's for P(x) = x < 5 Existential -∃x(P(x)) == ∀x(-P(x))
    reg = False
    dmorg = True
    for x in range(0,11): #loop for the regular function
        if x < 5:
            reg = True
            break
        else:
            reg = False
    for x in range(0,11): #loop for demorgan
        if x < 5 :
            dmorg = False
            break
        else:
            demorg = True
    if not reg == dmorg: #demorgan check
        return not reg, dmorg, True #inverse of the base functon, the demorganed function, and demorgan check
    else:
        return not reg, dmorg, False #inverse of the base functon, the demorganed function, and demorgan check
def f1():#Demorgan's for P(x) = x < 5 Universal -∀x(P(x)) == ∃x(-P(x))
    reg = False
    dmorg = True
    for x in range(0,11):# base loop
        if x >= 5:
            reg = False
            break
        else:
            reg = True
    for x in range(0,11):#demorg loop
        if x >= 5 :
            dmorg = True
            break
        else:
            demorg = False
    if not reg == dmorg:#demorg check
        return not reg, dmorg, True#inverse of the base functon, the demorganed function, and demorgan check
    else:
        return not reg, dmorg, False#inverse of the base functon, the demorganed function, and demorgan check
"""First problem end"""

"""Second problem functions and domain"""
domain = [1,2,4,5,10,0.5,0.25,0.2,0.1] #global list for the function's domain
def a2(): #∀x∀yP(x,y)
    for x in domain:
        for y in domain:
            if x * y != 1:
                return False, x, y #truth value of function, x where it is proven, y where it is proven
    return True, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
def b2():#∀x∃yP(x,y)
    count = 0
    for x in domain:
        for y in domain:
            if x * y == 1:
                count += 1
                break
            else:
                i = x
                j = y
    if count == len(domain):
        return True, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
    return False, i , j #truth value of function, x where it is proven, y where it is proven
def c2():#∀y∃xP(x,y)
    count = 0
    for y in domain:
        for x in domain:
            if x * y == 1:
                count += 1
                break
            else:
                i = x
                j = y
    if count == len(domain):
        return True, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
    return False, i, j #truth value of function, x where it is proven, y where it is proven
def d2():#∃x∀yP(x,y
    for x in domain:
        count = 0
        for y in domain:
            if x * y != 1:
                return False, x, y#truth value of function, x where it is proven, y where it is proven
            else:
                count += 1
        if count == len(domain):
            return True, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
    return False, i, j
def e2():#∃y∀xP(x,y)
    for y in domain:
        count = 0
        for x in domain:
            if x * y != 1:
                return False, x, y#truth value of function, x where it is proven, y where it is proven
            else:
                count += 1
        if count == len(domain):
            return True, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
    return False, i, j
def f2():#∃x∃yP(x,y)
    for x in domain:
        for y in domain:
            if x * y == 1:
                return True, x, y#truth value of function, x where it is proven, y where it is proven
    return False, 'all of the domain', 'all of the domain'#truth value of function, statement saying that it was consistent with the truth value for all of the domain
"""Second problem end"""

def main():#main prints out every function in a nice and readible way :)
    #first problem functions
    print("1a-1f all use the domain of {0,1,2,3,4,5,6,7,8,9,10}")
    print(f"1a) ∃xP(x) for when P(x) = x < 2 is: {a1()[0]} for x = {a1()[1]}")#∃xP(x) | P(x) = x < 2
    print(f"1b) ∀xP(x) for when P(x) = x < 2 is: {b1()[0]} for x = {b1()[1]}")#∀xP(x) | P(x) = x < 2 
    print(f"1c) ∃x(P(x) ∨ Q(x)) for when P(x) = x < 2 and when Q(x) = x > 7 is: {c1()[0]} for x = {c1()[1]}")#∃x(P(x) ∨ Q(x))| P(x) = x < 2 | Q(x) = x > 7
    print(f"1d) ∀x(P(x) ∨ Q(x)) for when P(x) = x < 2 and when Q(x) = x > 7 is: {d1()[0]} for x = {d1()[1]}")#∀x(P(x) ∨ Q(x)) | P(x) = x < 2 |  Q(x) = x > 7
    print(f"1e) Prove De Morgan's Law for ∃xP(x) where P(x) = x < 5: -∃xP(x) = {e1()[0]}, using demorgan the preious function equals, ∀x(-P(x)). ∀x(-P(x)) = {e1()[1]}, this shows that demorgan's is {e1()[2]}")
    print(f"1f) Prove De Morgan's Law for ∀xP(x) where P(x) = x < 5: -∀xP(x) = {f1()[0]}, using demorgan the preious function equals, ∃x(-P(x)). ∃x(-P(x)) = {f1()[1]}, this shows that demorgan's is {f1()[2]}")
    #second problem functions
    print("\nThe next statements use the domain of [1,2,4,5,10,0.5,0.25,0.2,0.1] for both x and y. P(x,y) = x * y = 1")
    print(f"2a) ∀x∀yP(x,y) with the given domain is: {a2()[0]} when x = {a2()[1]} and when y = {a2()[2]}")#∀x∀yP(x,y)
    print(f"2b) ∀x∃yP(x,y) with the given domain is: {b2()[0]} when x = {b2()[1]} and when y = {b2()[2]}")#∀x∃yP(x,y)
    print(f"2c) ∀y∃xP(x,y) with the given domain is: {c2()[0]} when x = {c2()[1]} and when y = {c2()[2]}")#∀y∃xP(x,y)
    print(f"2d) ∃x∀yP(x,y) with the given domain is: {d2()[0]} when x = {d2()[1]} and when y = {d2()[2]}")#∃x∀yP(x,y
    print(f"2e) ∃y∀xP(x,y) with the given domain is: {e2()[0]} when x = {e2()[1]} and when y = {e2()[2]}")#∃y∀xP(x,y)
    print(f"2f) ∃x∃yP(x,y) with the given domain is: {f2()[0]} when x = {f2()[1]} and when y = {f2()[2]}")#∃x∃yP(x,y)
main() #runs main
    
