print("Welcome to the multiplex")
you=input("enter your choice(stationary,digital library,reading room,music area,game zone):")
if you == "stationary":
    print("ok, please give me a minute !") 
    print("list of items: (moral,magazines,textbooks)")
    intrest=input("enter your intrest :")
    if intrest == "moral" or "magazines":
        print("oh!yes ,your search is here")
    elif intrest == "textbooks":
        print("oh!yes ,your search is here")
    else :
        print(f"Oh,There is no {intrest},choose another")
elif you == "digital library":
    print("ok ,wait let me open the door")
    system_number=int(input("enter your system number:"))
    if system_number <= 10:
        print("ok,let me check whether it is free r not")
        print("yes your system is free,now you can use")
    elif system_number > 10:
        print(f"sorry! {system_number} is not available. so, please enter below 10")
    else :
        print("invalid")
elif you == "reading room":
    print("ok, you can come")
    tables=input("enter your choice:(right side, left side)")
    if tables == "right side":
        print("yes!,its free to read")
    elif tables == "left side":
        print("sorry! it is occupied by others")
elif you == "music area":
    print("ok ,wait let me open the door")
    songs=(input("enter which type of songs you want to listen:"))
    if songs == "dj" or "folk songs":
        print("yes! your songs are ready,you can listen now")
    elif songs  ==  "movie songs":
        print("yes! your songs are ready .enjoy")
    else :
        print(f"sorry! {songs} is not available.")
elif you == "game zone":
    print(" Welcome to the game zone")
    import random

    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 10)  # Random number between 1 and 10
    guess = None

    while guess != number:
          guess = int(input("Guess a number between 1 and 10: "))
          if guess < number:
             print("Too low! Try again.")
          elif guess > number:
             print("Too high! Try again.")
    print("Congratulations! You guessed the number!")    
else:
    print(" you did't choose the valid choice.please choose (stationary,digital library,reading room,music room,:)")
    print("thanks for visting")
