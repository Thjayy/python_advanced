def guessNumber(startRange, endRange):
    if startRange > endRange:
        return True
    

    mid = (startRange + endRange)//2
     

    print("Is the number is ", mid, "?", end = " ")
    user = input()
    print(user)
     

    if user == "Y" or user == "y":
        print("Successfully Guessed Number.",)
        return False
         

    elif user == "N" or user == "n":
        print("Actual number is greater than",\
                        mid, "?", end = " ")
        user = input()
        print(user)
        if user == "Y" or user == "y":
            return guessNumber(mid+1, endRange)
        elif user == "N" or user == "n":
            return guessNumber(startRange, mid-1)
        else:
            print("Invalid Input. Print 'Y'/'N'")
            return guessNumber(startRange, endRange)
     
    else:
        print("Invalid Input. Print 'Y'/'N' ")
        return guessNumber(startRange, endRange)