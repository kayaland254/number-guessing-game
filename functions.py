def play(user_choice):
    stop_playing = False

    while not stop_playing:
        if user_choice == "yes":
            user_choice_number = int(input("Type any number that comes to mind.\n"))
            if user_choice_number % 2 == 0:
                print(f"{user_choice_number} is an even number.")
            else:
                print(f"{user_choice_number} is an odd number.")

            user_choice_keep_playing = input("Would you like to continue playing? yes or no?\n").lower()
            if user_choice_keep_playing == "yes":
                stop_playing = False
            else:
                stop_playing = True
                print("Thank you for playing!")
        else:
            print("Good bye!")
            break
