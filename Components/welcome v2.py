import random
from random import randint

#List of random names
names = ["James", "Phil", "Emma", "Philip", "Jacob", "Jayden", "Jill", "Ellen", "Laura","Eric" ]

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


def main():
    
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns:None
    '''
    welcome()

    main()