def menu():
    print("Choose the message : ")
    print("1. Hello, how are you?")
    print("2. What are you doing?")
    print("3. What is your name?")
    print("4. Goodbye!")

def choice():
    pilihan = int(input("Choose the message you want to sent: "))
    if pilihan == 1:
        print("Hi, I'm fine, thanks!")
    elif pilihan ==2:
        print("I'm Learning Programming")
    elif pilihan ==3:
        print("My name is Fharid-bot")
    elif pilihan==4:
        print("Goodbye!")
    else :
        print("Wrong input bro!")

def tryAgain():
    TryAgain = str(input("Try Again y/N : "))
    if TryAgain == "y" or TryAgain == "Y":
        menu()
        choice()
        tryAgain()
    elif TryAgain == "n" or TryAgain == "N":
        pass
    else:
        print("wrong input!")


        
menu()
choice()
tryAgain()
