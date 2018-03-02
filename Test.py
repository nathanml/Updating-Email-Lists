# Test Cases for changeList

from BroListClass import*

Bob = Brother("Bob", "b1234@bu.edu")
Phil = Brother("Phil", "philly@bu.edu")
Susie = Brother("Susie", "sss123@bu.edu")
Nathan = Brother("Nathan", "nathanml@bu.edu")

activeBros = emailList("Active Brothers")
activeBros.addBrother(Nathan)
activeBros.addBrother(Susie)
activeBros.addBrother(Phil)
activeBros.addBrother(Bob)

print(activeBros)

associateBros = emailList("Associate Brothers")
changeList(Bob, associateBros)

print(associateBros)
print(activeBros)

activeBros.printemailList()
