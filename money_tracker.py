while True:
    try:
        n = float(input("Money: "))
        exited = False
        while True:
            try:
                choice = str(input("Type of transaction? 1(paycheck); 2(pay): "))
                if choice == "1":
                    while True:
                        try:
                            x = float(input("Sum?: "))
                            n = n + x
                            break
                        except ValueError:
                            print("ValErr: inout must be a float.")
                elif choice == "2":
                    while True:
                        try:
                            x = float(input("Sum?: "))
                            n = n - x
                            break
                        except ValueError:
                            print("VallErr: input must be a float.")
                elif choice == "ls":
                    print(n)
                elif choice == "exit":
                    exited = True
                    break
                else:
                    print("Err: not a choice.")
            except ValueError:
                print("ValErr: input must be a string.") 
        if exited:
            break
    except ValueError:
        print("VallErr: input must be a float.")
