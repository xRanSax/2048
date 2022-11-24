# All the imports go here
import numpy as np


# move all the zeros to the right in O(N)
# modify array in place
# preserve original non-zero value orders
def move_zeros_right(nums):
    # two pointers
    # p1 iterate through the array
    # p2 points to 0
    p2 = 0
    for p1 in range(len(nums)):
        # if p1 points to non-zero, p2 points to 0 and
        if nums[p1] and not nums[p2] and p2 < p1:
            nums[p1], nums[p2] = nums[p2], nums[p1]
        # if p2 not point to 0, move p2
        if nums[p2]:
            p2 += 1


# similar to move_zero_right, but move all the zeros to the left
def move_zeros_left(nums):
    p2 = len(nums) - 1
    for p1 in range(len(nums) - 1, -1, -1):
        if nums[p1] and not nums[p2] and p2 > p1:
            nums[p1], nums[p2] = nums[p2], nums[p1]
        if nums[p2]:
            p2 -= 1


# a class that represent the game board
class Board:
    def __init__(self):
        # initialize a 4x4 matrix filled with 0
        self.board = np.zeros((4, 4), dtype=np.int)
        # initialize moves
        self.moves = {
            'w': self.move_up,
            's': self.move_down,
            'a': self.move_left,
            'd': self.move_right
        }
        # randomly put 2 '2' on the board
        # random generate the coordinates
        r1, c1 = np.random.randint(0, 4), np.random.randint(0, 4)
        r2, c2 = r1, c1
        while r2 == r1 and c2 == c1:
            r2, c2 = np.random.randint(0, 4), np.random.randint(0, 4)
        # insert value 2
        self.board[r1][c1] = self.board[r2][c2] = 2

    # execute user input and send the game to the next round
    def next_round(self, user_input):
        # before moving the board, record the board
        before_move = self.board.tostring()
        # perform the move based on user input
        self.moves[user_input]()
        # after the move, compare the new board with previous board
        after_move = self.board.tostring()
        # if the board did not change, user hit the wall
        # do not generate a new number and notify the user
        if before_move == after_move:
            return 2
        # add a new tile of 2 to a random empty tile
        # search for tile with value 0
        zero_index = np.where(self.board == 0)
        # randomly choose a tile
        random_index = np.random.randint(len(zero_index[0]))
        self.board[zero_index[0][random_index]][zero_index[1][random_index]] = 2
        # check the status of the board and return
        return self.status()

    # move numbers to left
    # corresponding to the 'a' input
    def move_left(self):
        # first group all non-zero tile to the left
        for i in range(4):
            move_zeros_right(self.board[i])
        # check from left to right
        # perform addition
        for i in range(4):
            for j in range(3):
                # if the tile is not empty and equals the tile on its right
                # add two tile
                if self.board[i][j] and self.board[i][j] == self.board[i][j + 1]:
                    self.board[i][j], self.board[i][j + 1] = self.board[i][j] * 2, 0
        # group all non-zero tile to the left again
        for i in range(4):
            move_zeros_right(self.board[i])

    # move numbers to right
    # corresponding to the 'd' input
    def move_right(self):
        # first group all non-zero tile to the right
        for i in range(4):
            move_zeros_left(self.board[i])
        # check from right to left
        # perform addition
        for i in range(4):
            for j in range(3, 0, -1):
                # if the tile is not empty and equals the tile on its left
                # add two tile
                if self.board[i][j] and self.board[i][j] == self.board[i][j - 1]:
                    self.board[i][j], self.board[i][j - 1] = self.board[i][j] * 2, 0
        # group all non-zero tile to the right again
        for i in range(4):
            move_zeros_left(self.board[i])

    # move number to top
    # corresponding to the 'w' input
    def move_up(self):
        # group all non-zero tile to the top
        for i in range(4):
            move_zeros_right(self.board[:, i])
        # check from top to bottom
        # perform addition
        for j in range(4):
            for i in range(3):
                # if the tile is not empty and equals the tile on its bottom
                # add two tile
                if self.board[i][j] and self.board[i][j] == self.board[i + 1][j]:
                    self.board[i][j], self.board[i + 1][j] = self.board[i][j] * 2, 0
        # group all non-zero tile to the top again
        for i in range(4):
            move_zeros_right(self.board[:, i])

    # move number to bottom
    # corresponding to the 's' input
    def move_down(self):
        # group all non-zero tile to the bottom
        for i in range(4):
            move_zeros_left(self.board[:, i])
        # check from bottom to top
        # perform addition
        for j in range(4):
            for i in range(3, 0, -1):
                # if the tile is not empty and equals the tile on its top
                # add two tile
                if self.board[i][j] and self.board[i][j] == self.board[i - 1][j]:
                    self.board[i][j], self.board[i - 1][j] = self.board[i][j] * 2, 0
        # group all non-zero tile to the bottom
        for i in range(4):
            move_zeros_left(self.board[:, i])

    # check the status of the board
    # -1 user lose, game terminated
    # 0 user can keep playing
    # 1 user wins, game terminated
    def status(self):
        # check if 2048 exist in the board
        if 2048 in self.board:
            return 1
        # check if the board is full
        # if it is not full, user can keep playing
        if 0 in self.board:
            return 0
        # if the board is full, check if there's movable pieces
        for i in range(4):
            for j in range(4):
                current_val = self.board[i][j]
                # check four directions to see possible matches
                if i-1 >= 0 and current_val == self.board[i-1][j]:
                    return 0
                if i+1 < 4 and current_val == self.board[i+1][j]:
                    return 0
                if j-1 >= 0 and current_val == self.board[i][j-1]:
                    return 0
                if j+1 < 4 and current_val == self.board[i][j+1]:
                    return 0
        return -1

    # override the default print function
    def __str__(self):
        # result string
        s = ''
        # iterate over each row
        for i in range(4):
            # create a substring for each row
            sub_string = '|'
            for j in range(4):
                # add value to substring
                if self.board[i][j]:
                    sub_string += '{:^4}|'.format(self.board[i][j])
                else:
                    sub_string += '{:^4}|'.format('')
            # add substring back to result string
            s = s + sub_string + '\n'
        return s
