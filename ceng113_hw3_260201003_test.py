# 260201003 Umutcan CEYHAN 
import ceng113_hw3_260201003 as functions
users = dict()
connectionCounter = 0
functions.addAUser("Sam",users)
functions.deleteAUser("Sam",users,connectionCounter)
functions.addAUser("Sam",users)
functions.addAUser("Toby",users)
functions.addAUser("Ella",users)
functions.addAUser("Jack",users)
functions.addAUser("Alice",users)
functions.addAUser("Bob",users)
functions.addAUser("Leo",users)
connectionCounter = functions.addAFriend("Ella","Toby",users,connectionCounter)
connectionCounter = functions.removeAFriend("Ella","Toby",users,connectionCounter)
connectionCounter = functions.addAFriend("Ella","Toby",users,connectionCounter)
connectionCounter = functions.addAFriend("Jack","Toby",users,connectionCounter)
connectionCounter = functions.addAFriend("Sam","Toby",users,connectionCounter)
connectionCounter = functions.addAFriend("Sam","Alice",users,connectionCounter)
connectionCounter = functions.addAFriend("Leo","Bob",users,connectionCounter)
connectionCounter = functions.addAFriend("Leo","Sam",users,connectionCounter)
connectionCounter = functions.addAFriend("Bob","Alice",users,connectionCounter)
connectionCounter = functions.addAFriend("Bob","Jack",users,connectionCounter)
print(functions.offerAFriend("Sam",users,connectionCounter))
