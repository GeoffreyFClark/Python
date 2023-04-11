from p1_random import P1Random  # import the class directly from the module
rng = P1Random()        # create a P1Random variable (do this in main)


def choice_menu():  # Menu function and takes user input
    print("\n1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit\n")
    return int(input("Choose an option: "))


def face_card_conversion(card_value):  # Gets name of face cards when 1, 11, 12, or 13 is randomly generated
    if card_value == 1:
        return "ACE"
    elif 2 <= card_value <= 10:
        return str(card_value)
    elif card_value == 11:
        return "JACK"
    elif card_value == 12:
        return "QUEEN"
    elif card_value == 13:
        return "KING"

games_played = 0
player_wins = 0
dealer_wins = 0
ties = 0
option = 0


while option != 4:  # 4 will be the option to exit the game
    print(f"\nSTART GAME #{games_played + 1}")
    drawn_card = rng.next_int(13) + 1  # A random number in range [1,13]
    print(f"\nYour card is a {face_card_conversion(drawn_card)}!")
    if drawn_card > 10:
        drawn_card = 10  # Sets value of jack, queen, or king to 10
    player_hand = drawn_card
    print(f"Your hand is: {player_hand}")

    while option != 4:
        option = choice_menu()
        if option == 1:  # If statement logic for when the player chooses to draw another card.
            drawn_card = rng.next_int(13) + 1  # A random number in range [1,13]
            print(f"\nYour card is a {face_card_conversion(drawn_card)}!")
            if drawn_card > 10:
                drawn_card = 10  # Sets value of jack, queen, or king to 10
            player_hand += drawn_card
            print(f"Your hand is: {player_hand}")
            if player_hand > 21:
                print("\nYou exceeded 21! You lose.")
                dealer_wins += 1
                break
            elif player_hand == 21:
                print("\nBLACKJACK! You win!")
                player_wins += 1
                break
        elif option == 2:  # Logic for when the player holds their hand into a showdown.
            dealer_hand = rng.next_int(11) + 16  # A random number in range [16,26]
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}\n")
            if dealer_hand > 21:
                print("You win!")
                player_wins += 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                ties += 1
            elif player_hand > dealer_hand:
                print("You win!")
                player_wins += 1
            elif dealer_hand > player_hand:
                print("Dealer wins!")
                dealer_wins += 1
            break
        elif option == 3:  # Game statistics at the player's request.
            print(f"\nNumber of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {games_played}")
            player_win_percentage = (player_wins / games_played) * 100
            print(f"Percentage of Player wins: {player_win_percentage:.1f}%")
        elif option == 4:  # Exits game: Breaks look, and another isn't started since option != 4 evaluates to false.
            break
        else:  # Error handling to catch invalid option choices.
            print("\nInvalid input!")
            print("Please enter an integer value between 1 and 4.")
    games_played += 1