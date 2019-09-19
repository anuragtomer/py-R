class Parent(object):

    def altered(self):
        print("Parent")

class Child(Parent):

    def altered(self):
        print("Child")
        super(Child, self).altered()
        print("Child again.")

dad = Parent()
son = Child()

dad.altered() # Prints Parent. Called parent.altered directly.
son.altered() # print child, parent, child. parent.altered called explicitly from child.alterned().