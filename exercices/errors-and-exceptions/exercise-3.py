def ask():
    while True:
        try:
            number = int(input("Please, input an integer number: "))
        except:
            print("Please try again!\n")
            continue
        else:
            break

    print(f"Thank you, your number squared is:  {number ** 2}")
    
ask()
