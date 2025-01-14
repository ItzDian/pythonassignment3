import os


class Journal:
    def __init__(self):
        """
        the constructor of the Journal task
        """
        self.title = ""
        self.author = ""

    def set_title(self, title):
        """
        The getter of the Journal task
        :param title: Used to set tittle for the journal
        :return: none
        """
        self.title = title

    def set_author(self, author):
        """
        The getter of the Journal task
        :param author: Used to name the author of the journal
        :return: none
        """
        self.author = author

    def create(self):
        """
        Create journal for the spaceship
        :return: none
        """
        self.set_title(input("Input the journal name: "))
        cwd = os.getcwd()  # Return a string representing the current working directory.
        path_file = cwd + '/' + self.title  # set path to variable path_file
        try:
            os.mkdir(path_file)
        except OSError:
            print("Creation of the directory %s failed" % path_file)
        else:
            print("Create successfully %s" % path_file)

    def open(self):
        """
        This function is used to open journals
        :return: none
        """

        os.chdir(os.getcwd())

        print("List of journal : {}".format(len(os.listdir())))
        print(*os.listdir())
        self.set_title(input("Input the journal name: "))
        os.chdir(os.getcwd() + "/" + self.title)

        page_list = os.listdir()
        print("Current pages:".format(len(page_list)))
        print(*page_list)

    def remove(self):
        """
        This function is used to remove a journal from the list
        :return: none
        """
        self.set_title(input("Input the name of journal: "))
        os.remove(self.title)
