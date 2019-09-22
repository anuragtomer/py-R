'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class inputOutput(object):

    def __init__(self):
        # Initialise instance variable to dummy.
        self.classString = ""

    def getString(self):
        # Read string from user
        self.classString = input()
    
    def printString(self):
        # print string in upper case
        print(self.classString.upper())

inp = inputOutput()
inp.getString()
inp.printString()