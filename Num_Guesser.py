while(True):
    import random
    n = random.randint(0, 60)
    print("~~~Welcome to number guessing game~~~")
    print("Rules:\n\t1)Choose number between 0 to 60\n\t2) You have only 9 chooses\n\t3)If you choose the correct one you will win else \'Game Over\'\n")
    print("Let's start the game:\n")
    i = 8
    for choose in range(0, 9):
        print("\nNumber of choice left: ", i+1)
        ch = input("Input your number: ")
        if ch.isnumeric():
            ch = int(ch)
            if ch > n:
                if choose == 8:
                    print("\n\'Game Over!\'The number is: ", n)
                    break
                print("Your number is biger than mine!\n")
                i = i-1
                continue
            elif ch < n:
                if choose == 8:
                    print("\n\'Game Over!\'The number is: ", n)
                    break
                print("Your number is lesser than mine!\n")
                i = i-1
                continue
            else:
                print("\nYep you got it You win!")
                print("Number of choice you took: ", i+1)
                break
        else:
            print("Please Enter a number!\n")
            i = i-1
            if choose == 8:
                print("\n\'Game Over!\'The number is: ", n)
                break
            continue
    s = input("\nEnter s for play again else enter any key: ")
    if s == "s":
        continue
    else:
        break
