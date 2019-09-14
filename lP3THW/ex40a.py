# NOTE: This file doesn't run directly. Needs some choice making to run based on 
# what in style you want to access data.

# dict style
mystuff = {'apple': "I AM APPLES!"}
mystuff['apples']

# module style
'''
# mystuff.py contents for module style:
def apple():
    print("I AM APPLES!")

tangerine = "Living reflection of a dream"
'''
mystuff.apples()
print(mystuff.tangerine)

# class style
'''
# mystuff.py contens for class style:
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")
'''
thing = MyStuff()
thing.apples()
print(thing.tangerine)
