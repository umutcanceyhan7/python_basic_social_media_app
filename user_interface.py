# 260201003 Umutcan CEYHAN
import system_functions as functions

# Users dictionary
users = dict()
connectionCounter = 0

# Interface for system
while True:
    print("Our network",users)
    print("Menu :")
    print("[1] Type 1 to add a user to network.")
    print("[2] Type 2 to delete a user from network.")
    print("[3] Type 3 to add a friend to a user.")
    print("[4] Type 4 to remove a friend from a user.")
    print("[5] Type 5 to offer a friend to a user.")
    print("[6] Type 6 to exit.")
    option = int(input("Please type a number: "))
    if(option == 1):
        username = input("Please type to user a username: ")
        functions.addAUser(username,users)
    elif(option == 2):
        username = input("Please type username that you want to delete from network: ")
        connectionCounter = functions.deleteAUser(username,users,connectionCounter)
    elif(option == 3):
        username1 = input("Please type the user that will add a friend to his/her friends: ")
        username2 = input("Please type the other user: ")
        connectionCounter = functions.addAFriend(username1,username2,users,connectionCounter)
    elif(option == 4):
        username1 = input("Please type the user that will remove a friend from his/her friends: ")
        username2 = input("Please type the other user that will be removed: ")
        connectionCounter = functions.removeAFriend(username1,username2,users,connectionCounter)
    elif(option == 5):
        username = input("Please type the user that will take the offer: ")
        print(functions.offerAFriend(username,users,connectionCounter))
    elif(option == 6):
        break
    else:
        print("You typed invalid number.")
    input("Please press any key to continue.")