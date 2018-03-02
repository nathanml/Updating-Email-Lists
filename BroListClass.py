# This defines the Brother class, which will store a string name, email address,
# and current list, which has the name of the current email list the brother is
# in.
class Brother():
    def __init__(self, name, address):
        'constructor for brother class'
        self.name = name
        self.address = address
        self.currentList = None

    def __repr__(self):
        'Returns a string representation for a Brother object.'
        s = ''      
        s += self.name + ': ' + self.address
        return s

    def changeList(self, List):
        'Modifies currentList attribute of Brother object'
        self.currentList = List

# The emailList class consists of a name and list of brothers. It has a
# constructor and repr method, as well as a method for adding a brother,
# removing a brother, and printing a list of just emails. This last method
# important because it makes it easy to use these lists to send emails.
class emailList():
        def __init__(self, name):
            'constructor for emailList class'
            self.name = name
            self.list = []

        def __repr__(self):
            'Returns a string representation for emailList object'
            s = ''
            s += self.name + ': ' + str(self.list)
            return s

        def addBrother(self, brother):
            'Adds a brother to an emailList'
            if brother not in self.list:
               self.list.append(brother)
               brother.currentList = self
            else:
                print("Brother already in list")

        def removeBrother(self, brother):
            'Removes a brother from an emailList'
            if brother in self.list:
                self.list.remove(brother)

        def changeList(self, brother, newList):
            'Moves a brother from its current list to a new list'
            self.removeBrother(brother)
            newList.addBrother(brother)
            brother.changeList(newList)
                
        def printemailList(self):
            'Will print just the emails of every brother in the list'
            #print( [brother.address.strip('"\'') for brother in self.list])
            for brother in self.list:
                print(brother.address + ",")
        

def changeList(brother, newList):
    'Moves a brother from its current list to a new list'
    brother.currentList.changeList(brother, newList)
