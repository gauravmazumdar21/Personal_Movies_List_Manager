movies = []

def menu():
    user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie, 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Wrong input, try again")

        user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie, 'q' to quit: ")



        


menu()