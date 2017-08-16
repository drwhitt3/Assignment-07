#!/usr/bin/env python
'''Assignment 7
Daniel Whitt
8/15/2017'''

from sortedcontainers import SortedDict
import sys
#importing necessary modules for this assignment

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()
#defining what print_menu() means

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
        #if the user inputs a valid number, then this continues

    except ValueError:
        print("Please only enter a number 1-5")
        sys.exit()
        #if the user enters a value that would cause an error, then they instead get the above message

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))
            #all current entries in the dictionary are printed

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            del usernames[name]
            #if the user wants to delete a valid name that is in the dictionary, then it is deleted
        else:
            print("No current user exists with the following name: {}".format(name))
            #if the user attempts to delete a name that is not in the dictionary, then they receive the above message

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print(usernames[name])
            #if the user is asking for a valid username, then it is printed
        else:
            print("This username is not found")
            #if the user is asking for a username that does not exist, then they receive the above message

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()