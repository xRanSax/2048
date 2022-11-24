# All the imports go here
from board import Board
# create a set of valid inputs
move_input = {'w', 'a', 's', 'd'}
yn_input = {'y', 'n', ''}

# greet the user
print('Welcome to 2048')

# start the game
# the game will keep running until user asked
while True:
    # initialize our board
    game_board = Board()
    # initialize our board status
    status = 0
    # show user the initial board
    print(game_board)
    # start this round of game
    # keep asking user for input
    # until the game is over
    while not status:
        # ask user for input
        user_input = input('Please enter you move: ')
        # handle invalid inputs
        while user_input.lower() not in move_input:
            user_input = input('Invalid input! You could only enter w, s, a, d\nPlease try to enter you move again: ')
        # send user input to board and update board status
        status = game_board.next_round(user_input.lower())
        # notify the user if their move does not change the board
        while status == 2:
            user_input = input('That move does not change the board. Please try another move: ')
            # handle invalid inputs
            while user_input.lower() not in move_input:
                user_input = input(
                    'Invalid input! You could only enter w, s, a, d\nPlease try to enter you move again: ')
            # update status
            status = game_board.next_round(user_input.lower())
        # show user the updated board
        print()
        print(game_board)
    # if the game reaches the end stage
    # inform user the game result and ask user if they want to play again
    if status == -1:
        user_input = input('The board is full. You loss. Wanna try again? [Y/N Default Y]')
    else:
        user_input = input('You achieved 2048! Wanna try again? [Y/N Default Y]')
    # handle invalid inputs
    while user_input.lower() not in yn_input:
        user_input = input('Invalid input!\nPlease enter Y or N')
    # if user do not want to play again
    # program terminated
    if user_input.lower() == 'n':
        print('Thank you for playing! Goodbye')
        break


