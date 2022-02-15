#Pizza Bot Program
import random
from random import randint

#List of random names
names = ["James", "Phil", "Emma", "Philip", "Jacob", "Jayden", "Jill", "Ellen", "Laura","Eric" ]

#Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")
#Menu for pickup delivery






#Pick up information- name and phone






#Delivery information - name, address and phone





#Choose Total Number of Pizzas - max 5






#Pizza menu






#Pizza order - from menu - print each pizza ordered with cost





#Print order out - including if order is delivery or pickup and names and price of each pizza - total cost including any delivery charge




#Ability to cancel or proceed with order





#Option for new order or to exit







#Main Function
def main():
    
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns:None
    '''
    welcome()

    main()