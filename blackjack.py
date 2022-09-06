# Importing rng file
import p1_random as p1

rng = p1.P1Random()


# Function for dealing a player card
def deal_card():
    new_card = rng.next_int(13) + 1

    if new_card == 1:
        return 1, 'ACE!'
    if new_card == 11:
        return 10, 'JACK!'
    if new_card == 12:
        return 10, 'QUEEN!'
    if new_card == 13:
        return 10, 'KING!'
    else:
        new_card_string = str(new_card) + '!'
        return new_card, new_card_string
# End of deal_card()


# Main function that runs
def main():
    # Declaring some variables
    num_games_played = 0
    player_games_won = 0
    dealer_games_won = 0
    num_ties = 0

    # New game loop
    while True:
        num_games_played += 1
        print(f'START GAME #{num_games_played}')
        hand_sum = 0
        new_card_num, new_card_name = deal_card()
        hand_sum += new_card_num
        print()
        print(f'Your card is a {new_card_name}')
        print(f"Your hand is: {hand_sum}")
        print()

        # Game options loop
        while True:
            print('1. Get another card')
            print('2. Hold hand')
            print('3. Print statistics')
            print('4. Exit')
            print()
            choice = int(input('Choose an option: '))

            # Get another card
            if choice == 1:
                new_card_num, new_card_name = deal_card()
                hand_sum += new_card_num
                print()
                print(f'Your card is a {new_card_name}')
                print(f'Your hand is: {hand_sum}')
                print()

                if hand_sum == 21:
                    print('BLACKJACK! You win!')
                    print()
                    player_games_won += 1
                    break
                if hand_sum >= 21:
                    print('You exceeded 21! You lose.')
                    print()
                    dealer_games_won += 1
                    break
                continue

            # Dealer gets hand
            if choice == 2:
                dealer_hand = rng.next_int(11) + 16
                print()
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {hand_sum}")
                print()

                # All possible situations after dealer gets hand
                if dealer_hand == 21:
                    print('Dealer wins!')
                    print()
                    dealer_games_won += 1
                    break
                if dealer_hand > 21:
                    print('You win!')
                    print()
                    player_games_won += 1
                    break
                if dealer_hand == hand_sum:
                    print("It's a tie! No one wins!")
                    num_ties += 1
                    print()
                    break
                if dealer_hand > hand_sum:
                    print('Dealer wins!')
                    print()
                    dealer_games_won += 1
                    break
                if hand_sum > dealer_hand:
                    print('You win!')
                    print()
                    player_games_won += 1
                    break
                continue

            # Display stats
            if choice == 3:
                win_percentage = (player_games_won / (num_games_played - 1)) * 100
                print()
                print(f'Number of Player wins: {player_games_won}')
                print(f'Number of Dealer wins: {dealer_games_won}')
                print(f'Number of tie games: {num_ties}')
                print(f'Total # of games played is: {num_games_played - 1}')
                print(f'Percentage of player wins: {win_percentage:.1f}%')
                print()
                continue

            # Exiting game
            if choice == 4:
                quit()

            # Checking for invalid inputs
            else:
                print()
                print('Invalid input!')
                print('Please enter an integer value between 1 and 4.')
                print()
        # End of game options loop
    # End of new game loop
# End of main()


main()
