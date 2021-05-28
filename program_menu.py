from journal import Journal

import os


def journal_menu(input_journal):
    """
    This function represent the menu of the journal
    :param input_journal: input the name of the journal
    :return: none
    """
    while True:
        print("--------Journal Menu----------")
        print("What would you like to do?: ")
        print("1: Create a journal")
        print("2: Open a journal")
        print("Type EXIT to close the program")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            input_journal.create_journal()
        elif option == "2":
            input_journal.open_journal()
        elif option.lower() == "exit":
            return False
        else:
            print("Please input 1-3 options: ")


# Menu
def spaceship_menu():
    """
    This function is used as a main menu to call other functions
    :return: none
    """
    while True:

        print("--------Spaceship Menu----------")
        print("1. Check overall spaceship ")
        print("2. Exit")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == '1':
            from basic_info import distance_and_time_cal
            print(distance_and_time_cal(225000000))
        elif option == "2":
            print('Stop the process')
            return False
        else:
            print("Please input 1-2 options: ")


def main_menu(input_journal):
    """
    This function represent the menu of the journal
    :param input_journal: input the name of the journal
    :return: none
    """

    while True:
        print("--------Main Menu----------")
        print("What would you like to do?: ")
        print("1: Open Spaceship Dashboard")
        print("2: Open Journal Dashboard")
        print("3: Open Binary Clock")
        print("EXIT to close the program")

        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            spaceship_menu()
        elif option == "2":
            journal_menu(input_journal)
        elif option == "3":
            from binary import binary_clock
            binary_clock()
        elif option.lower() == "exit":
            return False
        else:
            print("Please input 1-3 options: ")


# The condition when users type '__main__' instead of a page name or a journal name
if __name__ == '__main__':
    journal = Journal()
    author = input("Input your name: ")
    origin = os.getcwd()
    journal.set_author(author)
    print(""""
    ----------Welcome {} to HD spaceship (Group 32)------------
    Made by: 
    Nguyen Tuan Anh    (s3864077)
    Bui Quang An       (s3877482)
    Nguyen Ha Dieu Anh (s3879053)
    """.format(author))
    main_menu(journal)
