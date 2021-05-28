import datetime
import os
import glob


class Journal:
    def __init__(self):
        """
        constructor of the task
        """
        self.name = ""
        self.title = ""
        self.author = ""
        self.content = ""

    def set_name(self, name):
        """
        The setter of the Journal task
        :param name: Used to set tittle for the journal
        :return: none
        """
        self.name = name

    def set_title(self, title):
        """
        The setter of the Journal task
        :param title: Used to set tittle for the journal
        :return: none
        """
        self.title = title

    def set_author(self, author):
        """
        The setter of the Journal task
        :param author: Used to name the author of the journal
        :return: none
        """
        self.author = author

    def create_journal(self):
        """
        Create journal for the spaceship
        :return: none
        """
        self.set_name(input("Input the file name(Only name): "))
        self.set_title(input("Input the title: "))
        self.content = self.write()
        filename = self.name.replace(" ", "") + ".txt"
        entry = open(filename, "a")
        entry.write("Author: " + self.author + "\n")
        entry.write("Title: " + self.title + "\n")
        entry.write("Time: " + str(datetime.datetime.now()) + "\n")
        entry.write("Content: " + self.content)
        entry.close()

    def open_journal(self):
        """
        open a page
        :return: none
        """
        print(glob.glob('*.txt'))  # list all file txt
        self.set_title(input("Input the journal name(Only Name): "))
        filename = self.title.replace(" ", "") + ".txt"
        entry = open(filename, "r")
        print(*entry)
        while True:
            option = input("Enter Y for exit:  ")
            if option.lower() == 'y':
                return False
            else:
                print("Invalid argument")

    def write(self):
        """
        write a body of a note/paragraph or any kind of text in a page
        :return: self.content
        """
        self.content = input("Body: ")
        return self.content

    def remove(self):
        """
        Remove a page from the list
        :return: none
        """
        print(glob.glob('*.txt'))  # list all file txt
        self.set_name(input("Input the name of a page: "))
        filename = self.name.replace(" ", "") + ".txt"
        os.remove(filename)
