class Other(object):

    def override(self):
        print("Other override.")
    
    def implicit(self):
        print("Other Implicit.")
    
    def altered(self):
        print("Other altered.")

class Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("Child override.")
    
    def altered(self):
        print("Child before other.")
        self.other.altered()
        print("Child after other.")

son = Child()
son.implicit()
son.override()
son.altered()