"""
Assignment No. 1 
EECS 210
Alexander Carrillo
Date Created: 1/23/24

"""
import operator #Imports operator class for operator.not_ specificly 

def biconditional(x,y): #Function for biconditionals 
    if x == y: #reverse XOR
        return True #returns true
    else: #second condition
        return False #returns false

def implication(x,y): #Function for implications 
    if x == True and y == False: # Only returns Flase if x is True and y is False
        return False #returns False
    else: #second condition 
        return True #returns true
    
def main(): #Main holds 2d lists for twoterms and threeterm selections, the user menu, and all the table building for each selection
    twoterm = [[True,True],[True,False],[False,True],[False,False]] #For options 1,2, and 6
    threeterm = [[True,True,True],[True,True,False],[True,False,True],[True,False,False],[False,True,True],[False,True,False],[False,False,True],[False,False,False]] #For the associative laws and option 5
    while True: #infinte loop that runs the menu allowing for the user to try different options 
        print("1) De Morgan's First Law\n2) De Morgan's Second Law\n3) First Associative Law\n4) Second Associative Law\n5)[(p+q)*(p->r)*(q->r)]->r=T\n6) p<->q = (p->q)*(q->p)") #prints the menu
        userin = input("Please make a selection(1-6): ")#User input
        """User input options"""
        if userin == '1': #De Morgan's First Law
            print('\np\tq\t!{p*q)\t!p+!q') #prits the first line of the table
            for i in twoterm:#iterates through twoterm
                print(f"{i[0]}\t{i[1]}\t{operator.not_(i[0] and i[1])}\t{operator.not_(i[0]) or operator.not_(i[1])}")#Prints line by line for demorgan's first law
            print('\n')#new line
        elif userin == '2': #De Morgan's Second Law
            print('\np\t q\t!(p+q)\t!p*!q') #prits the first line of the table
            for i in twoterm:#iterates through twoterm
                print(f"{i[0]}\t{i[1]}\t{operator.not_(i[0] or i[1])}\t{operator.not_(i[0]) and operator.not_(i[1])}")#Prints line by line for demorgan's second law
            print('\n')#new line
        elif userin == '3': #First Associative Law
            print('\np\tq\tr\t(p*q)*r\tp*(q*r)') #prits the first line of the table
            for i in threeterm:#iterates through threeterm
                print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[0] and (i[1] and i[2])}\t{(i[0] and i[1]) and i[2]}")#Prints line by line for the first associative law
            print('\n')#new line
        elif userin == '4': #Second Associative Law
            print('\np\tq\tr\t(p+q)+r\tp+(q+r)') #prits the first line of the table
            for i in threeterm:#iterates through threeterm
                print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[0] or (i[1] or i[2])}\t{(i[0] or i[1]) or i[2]}")#Prints line by line for the second associative law
            print('\n')#new line
        elif userin == '5': #[(p + q)*(p -> r)*(q -> r)] -> r = T : Uses implications
            print('\np\tq\tr\t(p+q)\t(p->r)\t(q->r)\t[(p+q)*(p->r)*(q->r)]->r\tT') #prits the first line of the table
            for i in threeterm:#iterates through threeterm
                print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[0] or i[1]}\t{implication(i[0],i[2])}\t{implication(i[1],i[2])}\t{implication((i[0] or i[1]) and implication(i[0],i[2]) and (implication(i[1],i[2])),i[2])}\t{True}")#each line of the table for [(p + q)*(p -> r)*(q -> r)] -> r = T 
            print('\n') #new line
        elif userin == '6': #p <-> q = (p -> q)*(q -> p): Biconditional and implications 
            print("\np\tq\tp<->q\tp->q\tq->p\t(p->q)*(q->p)") #prits the first line of the table
            for i in twoterm:#iterates through twoterm
                print(f"{i[0]}\t{i[1]}\t{biconditional(i[0],i[1])}\t{implication(i[0],i[1])}\t{implication(i[1],i[0])}\t{implication(i[0],i[1]) and implication(i[1],i[0])}") #each line of the table for p <-> q = (p -> q)*(q -> p)
            print('\n') #new line
        else: #If the user doesn't enter a valid selection
            print("Plese make a valid selection") #aks the user to enter a valid selection
    
main()#runs main  
