class Parent(object):

    def override(self):
        print("Parent override.")
    
    def implicit(self):
        print("Parent implicit.")
    
    def altered(self):
        print("Parent altered.")

class Child(Parent):

    def override(self):
        print("Child override.")
    
    def altered(self):
        print("Child before parent.")
        super(Child, self).altered() # parent.altered()
        print("Child after parent.")

dad = Parent()
son = Child()

dad.implicit() # Calls parent.implicit
son.implicit() # No implicit defined in child. So parent's called.

dad.override() # parent.override
son.override() # child.override

dad.altered() # parent.altered
son.altered() # child.altered
