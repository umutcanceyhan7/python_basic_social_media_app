# 260201003 Umutcan CEYHAN
def recursiveFactorial(n):
    if n == 0:
        return 1
    else:
        return (n * recursiveFactorial(n - 1))
def combination(upperValue,lowerValue):
    combination = recursiveFactorial(upperValue)/(recursiveFactorial(upperValue-lowerValue)*recursiveFactorial(lowerValue))
    return combination
def addAUser(username,listname):
    username = username.capitalize()
    if username in listname:
        print("Sorry this username already exists.")
    else:   
        listname.update({username:[]})
        print(str(username)+" added to network.")
def deleteAUser(username,listname,connectionCounter):
    username = username.capitalize()
    if not username in listname:
        print("Sorry this user does not exist in the network.")
    else:
        removingPersons = listname.pop(username)  # Removing user's friends
        for person in removingPersons:
            friendslist = listname.get(person)
            friendslist.remove(username)
            listname.update({person:friendslist})
        print(username , "deleted from network.")
        connectionCounter -= len(removingPersons)
        return connectionCounter
def addAFriend(username1,username2,listname,connectionCounter):
    username1 = username1.capitalize()
    username2 = username2.capitalize()
    if not username1 in listname:
        print("One of the users or both are not in network")
    elif not username2 in listname:
        print("One of the users or both are not in network")
    else:
        if not username1 in listname.get(username2):        
            friendslist1 = listname.get(username1)     # Adding username2 to username1's friendslist
            friendslist1.append(username2)
            listname.update({username1:friendslist1})  #--------------------------------------------------------------------------------------------------------------------------------------
            friendslist2 = listname.get(username2)      # Adding username1 to username2's friendslist
            friendslist2.append(username1)
            listname.update({username2:friendslist2})  #--------------------------------------------------------------------------------------------------------------------------------------
            connectionCounter += 1
            print(str(username1)+ " is friend of " + str(username2) + " now.") 
            return connectionCounter
        else:
            print("They have already been friends or users are not in network.")
def removeAFriend(username1,username2,listname,connectionCounter):
    username1 = username1.capitalize()
    username2 = username2.capitalize()
    # Check if user1 is in network or not
    if not username1 in listname:
        print("They are not friends or users are not in network")
    # Check if user2 is in network or not
    elif not username2 in listname:
        print("They are not friends or users are not in network")
    # If both are in network
    else:
        # Check friendship by checking one of the user's friendslist
        if not username1 in listname.get(username2):
            print("They are not friends or users are not in network")
        # If they are friends remove their relationship between.
        else:    
            friendslist1 = listname.get(username1)   # Removing username2 from username1's friendslist
            friendslist1.remove(username2)
            listname.update({username1:friendslist1}) #--------------------------------------------------------------------------------------------------------------------------------
            friendslist2 = listname.get(username2)   # Removing username1 from username2's friendslist
            friendslist2.remove(username1)
            listname.update({username2:friendslist2}) #--------------------------------------------------------------------------------------------------------------------------------
            print(str(username1)+" and "+str(username2)+" are not friends now.")
            connectionCounter -= 1
    return connectionCounter
def offerAFriend(username,listname,connectionCounter):
    username = username.capitalize()
    notConnectedPeople = combination(len(listname),2) - connectionCounter # Possible users match amount - Users that has friend connection = Not CONNECTED PEOPLE
    wholePersons = set()                #Whole Persons
    matchesOfNotConnectedPeople = set()   # Whole Matches
    matchesOfOurUser = set()            # Our User's set
    #----------------------------------- Not CONNECTED MATCH SET and Whole Persons SET
    for i in listname.keys():
        wholePersons.add(i)             # Whole Persons filled up
    for user in wholePersons:
        friendOfUser = set(listname.get(user))
        friendOfUser.add(user)
        notFriendWithUser = wholePersons.difference(friendOfUser)   
        for match in notFriendWithUser:
            matchesOfNotConnectedPeople.add((user,match))     # Full matches like permutation
            matchesOfNotConnectedPeople.discard((match,user))   # Full matches as formatted combination
            if username == user:
                matchesOfOurUser.add((username,match))  # Our users matches
    minMaxCalculatorScale1 = []
    minMaxCalculatorScale2 = []
    ourUsersMatchesScale1 = []
    ourUsersMatchesScale2 = []
    scale1xList = []
    scale1Name1List = []
    scale1Name2List = []
    scale2xList = []
    scale2Name1List = []
    scale2Name2List = []
    for j in matchesOfNotConnectedPeople:
        commonFriends = 0
        matchListForm = list(j)
        firstUserFriends = set(listname.get(matchListForm[0])) #First user's friend
        secondUserFriends = set(listname.get(matchListForm[1])) #Second user's friend
        sumOfFriends = len(firstUserFriends) + len(secondUserFriends) - len(firstUserFriends.intersection(secondUserFriends)) #sumOfTheirFriends
        if(list(j)[0] == username or list(j)[1] == username):                                           # Our user's values with name
            for first in firstUserFriends:
                for second in secondUserFriends:
                    if(first == second):
                        commonFriends += 1
            ourUsersMatchesScale1.append([(commonFriends),list(j)[0],list(j)[1]])    
            ourUsersMatchesScale2.append([commonFriends/sumOfFriends,list(j)[0],list(j)[1]])        # -----------------------------------------------------
        else:                                                                                               
            for first in firstUserFriends:
                for second in secondUserFriends:
                    if(first == second):
                        commonFriends += 1                          
        minMaxCalculatorScale1.append(commonFriends)
        minMaxCalculatorScale2.append(commonFriends/sumOfFriends)
    
    for t in range(len(ourUsersMatchesScale1)):
        scale1xList.append(ourUsersMatchesScale1[t][0])
        scale1Name1List.append(ourUsersMatchesScale1[t][1])
        scale1Name2List.append(ourUsersMatchesScale1[t][2])
        scale2xList.append(ourUsersMatchesScale2[t][0])
        scale2Name1List.append(ourUsersMatchesScale2[t][1])
        scale2Name2List.append(ourUsersMatchesScale2[t][2])
    scale1min = min(minMaxCalculatorScale1)
    scale1max = max(minMaxCalculatorScale1)
    scale2min = min(minMaxCalculatorScale2)
    scale2max = max(minMaxCalculatorScale2)
    scale1x = max(scale1xList)
    scale2x = max(scale2xList)
    scale1xIndex = scale1xList.index(max(scale1xList))
    scale1Name1 = scale1Name1List[scale1xIndex]
    scale1Name2 = scale1Name2List[scale1xIndex]
    scale2xIndex = scale2xList.index(max(scale2xList))
    scale2Name1 = scale2Name1List[scale2xIndex]
    scale2Name2 = scale2Name2List[scale2xIndex]
    
    if (scale1min == scale1max):
        scale1 = (scale1x - scale1min)/ (0.5) 
    else:
        scale1 = (scale1x - scale1min)/ (scale1max - scale1min ) 
    if (scale2min == scale2max): 
        scale2 = (scale2x - scale2min)/ (0.5)
    else:
        scale2 = (scale2x - scale2min)/ (scale2max - scale2min)  
    if(scale1Name1 == username):
        offeredFriend = scale1Name2
    else:
        offeredFriendFromScale1 = scale1Name1
    if(scale2Name1 == username):
        offeredFriendFromScale2 = scale2Name2
    else:
        offeredFriendFromScale2 = scale2Name1
        if(offeredFriendFromScale1 == offeredFriendFromScale2):
            offeredFriend = offeredFriendFromScale1
        else:
            offeredFriend = offeredFriendFromScale2
    averageScale = (scale1 + scale2) / 2 
    return offeredFriend + " is offered to "+str(username)+" as rate " + str(averageScale)