# Author: Peter Battisti
# GitHub username: peterb3
# Date: 3/12/2024
# Description: This program is a fully functioning Falcon-Hunter Chess game, playable in the python console.
#       It ensures all moves are legal for each piece and allows a user/users to play a game to completion, when a
#       player's king is captured. If any input is invalid, it returns False.


class ChessVar:
    """
    This class represents a game of falcon-hunter chess that keeps track of the game state, turn, and board as private
    data members. Pieces are stored on the board as specific Piece objects defined in the __init__ method. This class
    has methods to return the game state, check whether a win has occurred, make a move for a piece, display the board,
    and enter a fairy piece.
    """
    def __init__(self):
        """
        This __init__ method defines the private data members game_state, which determines whether the game is
        ongoing, white has won, or black has won and is initialized to "not started", turn, which determines which
        player's turn it is and is initialized to "WHITE", and board, which defines a dictionary where each key is the
        name of each board position in order and the value for each key is initialized to None. Then, there is a check
        for if the game_state is "not started" (which it will be upon starting), then sets the game_state to
        "UNFINISHED" and initializes all the chess pieces, sets their colors, and places them in their correct board
        positions in the board private data member.
        """
        self._game_state = "not started"
        self._turn = "WHITE"
        self._board = {
            "a1": None, "a2": None, "a3": None, "a4": None, "a5": None, "a6": None, "a7": None, "a8": None,
            "b1": None, "b2": None, "b3": None, "b4": None, "b5": None, "b6": None, "b7": None, "b8": None,
            "c1": None, "c2": None, "c3": None, "c4": None, "c5": None, "c6": None, "c7": None, "c8": None,
            "d1": None, "d2": None, "d3": None, "d4": None, "d5": None, "d6": None, "d7": None, "d8": None,
            "e1": None, "e2": None, "e3": None, "e4": None, "e5": None, "e6": None, "e7": None, "e8": None,
            "f1": None, "f2": None, "f3": None, "f4": None, "f5": None, "f6": None, "f7": None, "f8": None,
            "g1": None, "g2": None, "g3": None, "g4": None, "g5": None, "g6": None, "g7": None, "g8": None,
            "h1": None, "h2": None, "h3": None, "h4": None, "h5": None, "h6": None, "h7": None, "h8": None
        }
        if self._game_state == "not started":
            self._game_state = "UNFINISHED"
            wpawn1 = Pawn()
            wpawn1.assign_color("WHITE")
            wpawn2 = Pawn()
            wpawn2.assign_color("WHITE")
            wpawn3 = Pawn()
            wpawn3.assign_color("WHITE")
            wpawn4 = Pawn()
            wpawn4.assign_color("WHITE")
            wpawn5 = Pawn()
            wpawn5.assign_color("WHITE")
            wpawn6 = Pawn()
            wpawn6.assign_color("WHITE")
            wpawn7 = Pawn()
            wpawn7.assign_color("WHITE")
            wpawn8 = Pawn()
            wpawn8.assign_color("WHITE")
            self._board["a2"] = wpawn1
            self._board["b2"] = wpawn2
            self._board["c2"] = wpawn3
            self._board["d2"] = wpawn4
            self._board["e2"] = wpawn5
            self._board["f2"] = wpawn6
            self._board["g2"] = wpawn7
            self._board["h2"] = wpawn8

            bpawn1 = Pawn()
            bpawn1.assign_color("BLACK")
            bpawn2 = Pawn()
            bpawn2.assign_color("BLACK")
            bpawn3 = Pawn()
            bpawn3.assign_color("BLACK")
            bpawn4 = Pawn()
            bpawn4.assign_color("BLACK")
            bpawn5 = Pawn()
            bpawn5.assign_color("BLACK")
            bpawn6 = Pawn()
            bpawn6.assign_color("BLACK")
            bpawn7 = Pawn()
            bpawn7.assign_color("BLACK")
            bpawn8 = Pawn()
            bpawn8.assign_color("BLACK")
            self._board["a7"] = bpawn1
            self._board["b7"] = bpawn2
            self._board["c7"] = bpawn3
            self._board["d7"] = bpawn4
            self._board["e7"] = bpawn5
            self._board["f7"] = bpawn6
            self._board["g7"] = bpawn7
            self._board["h7"] = bpawn8

            wrook1 = Rook()
            wrook1.assign_color("WHITE")
            wrook2 = Rook()
            wrook2.assign_color("WHITE")

            self._board["a1"] = wrook1
            self._board["h1"] = wrook2

            wknight1 = Knight()
            wknight1.assign_color("WHITE")
            wknight2 = Knight()
            wknight2.assign_color("WHITE")

            self._board["b1"] = wknight1
            self._board["g1"] = wknight2

            wbishop1 = Bishop()
            wbishop1.assign_color("WHITE")
            wbishop2 = Bishop()
            wbishop2.assign_color("WHITE")

            self._board["c1"] = wbishop1
            self._board["f1"] = wbishop2

            wqueen = Queen()
            wqueen.assign_color("WHITE")

            self._board["d1"] = wqueen

            wking = King()
            wking.assign_color("WHITE")

            self._board["e1"] = wking

            brook1 = Rook()
            brook1.assign_color("BLACK")
            brook2 = Rook()
            brook2.assign_color("BLACK")

            self._board["a8"] = brook1
            self._board["h8"] = brook2

            bknight1 = Knight()
            bknight1.assign_color("BLACK")
            bknight2 = Knight()
            bknight2.assign_color("BLACK")

            self._board["b8"] = bknight1
            self._board["g8"] = bknight2

            bbishop1 = Bishop()
            bbishop1.assign_color("BLACK")
            bbishop2 = Bishop()
            bbishop2.assign_color("BLACK")

            self._board["c8"] = bbishop1
            self._board["f8"] = bbishop2

            bqueen = Queen()
            bqueen.assign_color("BLACK")

            self._board["d8"] = bqueen

            bking = King()
            bking.assign_color("BLACK")

            self._board["e8"] = bking

    def get_game_state(self):
        """
        Returns the private data member game_state.
        """
        return self._game_state

    def check_for_win(self):
        """
        This function builds a list of both white and black pieces, then checks each collection for whether the King
        is still there. If it is not, it set the game state private data member to "WHITE_WON" if the black king is
        gone or "BLACK_WON" if the white king is gone.
        """
        white_pieces = []
        black_pieces = []
        for key in self._board:
            if self._board[key] is None:
                continue

            else:
                if self._board[key].get_color() == "WHITE":
                    white_pieces.append(self._board[key].label())

                else:
                    black_pieces.append(self._board[key].label())

        if "k" not in black_pieces:
            self._game_state = "WHITE_WON"
        if "K" not in white_pieces:
            self._game_state = "BLACK_WON"
        else:
            return False

    def make_move(self, curr_pos, next_pos):  # separate this into multiple piece-specific helper functions
        """
        This function outlines legal moves for every piece on the chess board. It creates a list for every position on
        the board, a list of list for each row on the board, a list of lists for each column on the board, and a list
        of lists for each diagonal on the board. The function ensures that both passed parameters are on the board,
        the positions aren't the same, there is a piece in the first position passed, that it's the correct turn for
        the piece listed, and that the game isn't over as baselines. Then depending on the color of the piece, it
        determines which piece is moving, how that piece should move to the next space if it's legal, and executes the
        move if there are no issues, capturing the piece in the next square if necessary, and returns True. If any part
        of the move is illegal, it returns False. Legal moves for each piece, white and black, are outlined in this
        method to cover all possible moves.
        :param curr_pos: Current position of piece being moved
        :param next_pos: Next position the piece needs to move to.
        :return: If legal move is entered, the piece is moved to new location and board private data member is updated
                and returns True, otherwise it returns False.
        """
        position_list = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
                         "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
                         "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
                         "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
                         "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
                         "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
                         "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
                         "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8",
                         ]
        columns_list = [["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"],
                        ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"],
                        ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"],
                        ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"],
                        ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"],
                        ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"],
                        ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8"],
                        ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"],
                        ]
        rows_list = [["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
                     ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                     ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                     ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                     ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                     ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                     ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                     ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                     ]
        diagonal_list = [["a8"],
                         ["a7", "b8"],
                         ["a6", "b7", "c8"],
                         ["a5", "b6", "c7", "d8"],
                         ["a4", "b5", "c6", "d7", "e8"],
                         ["a3", "b4", "c5", "d6", "e7", "f8"],
                         ["a2", "b3", "c4", "d5", "e6", "f7", "g8"],
                         ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"],
                         ["b1", "c2", "d3", "e4", "f5", "g6", "h7"],
                         ["c1", "d2", "e3", "f4", "g5", "h6"],
                         ["d1", "e2", "f3", "g4", "h5"],
                         ["e1", "f2", "g3", "h4"],
                         ["f1", "g2", "h3"],
                         ["g1", "h2"],
                         ["h1"],
                         ["a1"],
                         ["b1", "a2"],
                         ["c1", "b2", "a3"],
                         ["d1", "c2", "b3", "a4"],
                         ["e1", "d2", "c3", "b4", "a5"],
                         ["f1", "e2", "d3", "c4", "b5", "a6"],
                         ["g1", "f2", "e3", "d4", "c5", "b6", "a7"],
                         ["h1", "g2", "f3", "e4", "d5", "c6", "b7", "a8"],
                         ["h2", "g3", "f4", "e5", "d6", "c7", "b8"],
                         ["h3", "g4", "f5", "e6", "d7", "c8"],
                         ["h4", "g5", "f6", "e7", "d8"],
                         ["h5", "g6", "f7", "e8"],
                         ["h6", "g7", "f8"],
                         ["h7", "g8"],
                         ["h8"]
                         ]
        if curr_pos not in self._board or next_pos not in self._board:
            return False
        if curr_pos == next_pos:
            return False
        if self._board[curr_pos] is None:
            return False
        if self._board[curr_pos].get_color() == "WHITE" and self._turn == "BLACK":
            return False
        if self._board[curr_pos].get_color() == "BLACK" and self._turn == "WHITE":
            return False
        if self._game_state == "WHITE_WON" or self._game_state == "BLACK_WON":
            return False
        else:
            if self._board[curr_pos].get_color() == "WHITE":
                if self._board[curr_pos].label() == "P":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if (position_list[pos + 1] == next_pos or
                                    position_list[pos + 2] == next_pos or
                                    position_list[pos - 7] == next_pos or
                                    position_list[pos + 9] == next_pos):
                                if position_list[pos + 1] == next_pos and "8" not in curr_pos:
                                    if self._board[next_pos] is None:
                                        self._board[curr_pos].set_move_history(next_pos)
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                    else:
                                        return False
                                if position_list[pos + 2] == next_pos and self._board[curr_pos].get_move_history() is None:
                                    if self._board[position_list[pos + 1]] is None:
                                        if self._board[next_pos] is None:
                                            self._board[curr_pos].set_move_history(next_pos)
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                                    else:
                                        return False
                                if position_list[pos + 9] == next_pos and "8" not in curr_pos and "h" not in curr_pos:
                                    if self._board[position_list[pos + 9]] is None:
                                        return False
                                    if self._board[position_list[pos + 9]].get_color() == "BLACK":
                                        self._board[curr_pos].set_move_history(next_pos)
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                    else:
                                        return False
                                if position_list[pos - 7] == next_pos and "8" not in curr_pos and "a" not in curr_pos:
                                    if self._board[position_list[pos - 7]] is None:
                                        return False
                                    if self._board[position_list[pos - 7]].get_color() == "BLACK":
                                        self._board[curr_pos].set_move_history(next_pos)
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                if self._board[curr_pos].label() == "B":
                    for diagonal in diagonal_list:
                        if curr_pos in diagonal and next_pos in diagonal:
                            for index, position in enumerate(diagonal):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "R":
                    for row in rows_list:
                        if curr_pos in row and next_pos in row:
                            for index, position in enumerate(row):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    for column in columns_list:
                        if curr_pos in column and next_pos in column:
                            for index, position in enumerate(column):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "Q":
                    for diagonal in diagonal_list:
                        if curr_pos in diagonal and next_pos in diagonal:
                            for index, position in enumerate(diagonal):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    for row in rows_list:
                        if curr_pos in row and next_pos in row:
                            for index, position in enumerate(row):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    for column in columns_list:
                        if curr_pos in column and next_pos in column:
                            for index, position in enumerate(column):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "BLACK"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "N":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if "7" not in curr_pos and "8" not in curr_pos:
                                if "h" not in curr_pos:
                                    if next_pos == position_list[pos + 10]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                                if "a" not in curr_pos:
                                    if next_pos == position_list[pos - 6]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                            if "8" not in curr_pos:
                                if "a" not in curr_pos and "b" not in curr_pos:
                                    if next_pos == position_list[pos - 15]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                                if "g" not in curr_pos and "h" not in curr_pos:
                                    if next_pos == position_list[pos + 17]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                            if "1" not in curr_pos:
                                if "a" not in curr_pos and "b" not in curr_pos:
                                    if next_pos == position_list[pos - 17]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                                if "g" not in curr_pos and "h" not in curr_pos:
                                    if next_pos == position_list[pos + 15]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                            if "1" not in curr_pos and "2" not in curr_pos:
                                if "a" not in curr_pos:
                                    if next_pos == position_list[pos - 10]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                                if "h" not in curr_pos:
                                    if next_pos == position_list[pos + 6]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "BLACK"
                                            self.check_for_win()
                                            return True
                    else:
                        return False
                if self._board[curr_pos].label() == "K":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if "8" not in curr_pos and "a" not in curr_pos:
                                if next_pos == position_list[pos - 7]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "8" not in curr_pos:
                                if next_pos == position_list[pos + 1]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "8" not in curr_pos and "h" not in curr_pos:
                                if next_pos == position_list[pos + 9]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "a" not in curr_pos:
                                if next_pos == position_list[pos - 8]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "h" not in curr_pos:
                                if next_pos == position_list[pos + 8]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos and "a" not in curr_pos:
                                if next_pos == position_list[pos - 9]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos:
                                if next_pos == position_list[pos - 1]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos and "h" not in curr_pos:
                                if next_pos == position_list[pos + 7]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                    else:
                        return False
                if self._board[curr_pos].label() == "H":
                    curr_row = None
                    next_row = None
                    for index, row in enumerate(rows_list):
                        if curr_pos in row:
                            curr_row = index
                        if next_pos in row:
                            next_row = index
                    if curr_row == next_row:
                        return False
                    if curr_row < next_row:
                        for column in columns_list:
                            if curr_pos in column and next_pos in column:
                                for index, position in enumerate(column):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    if curr_row > next_row:
                        for diagonal in diagonal_list:
                            if curr_pos in diagonal and next_pos in diagonal:
                                for index, position in enumerate(diagonal):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    else:
                        return False
                if self._board[curr_pos].label() == "F":
                    curr_row = None
                    next_row = None
                    for index, row in enumerate(rows_list):
                        if curr_pos in row:
                            curr_row = index
                        if next_pos in row:
                            next_row = index
                    if curr_row == next_row:
                        return False
                    if curr_row < next_row:
                        for diagonal in diagonal_list:
                            if curr_pos in diagonal and next_pos in diagonal:
                                for index, position in enumerate(diagonal):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    if curr_row > next_row:
                        for column in columns_list:
                            if curr_pos in column and next_pos in column:
                                for index, position in enumerate(column):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "BLACK":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "BLACK"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            if self._board[curr_pos].get_color() == "BLACK":
                if self._board[curr_pos].label() == "p":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if (position_list[pos - 1] == next_pos or
                                    position_list[pos - 2] == next_pos or
                                    position_list[pos + 7] == next_pos or
                                    position_list[pos - 9] == next_pos):
                                if position_list[pos - 1] == next_pos and "1" not in curr_pos:
                                    if self._board[next_pos] is None:
                                        self._board[curr_pos].set_move_history(next_pos)
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                    else:
                                        return False
                                if position_list[pos - 2] == next_pos and self._board[curr_pos].get_move_history() is None:
                                    if self._board[position_list[pos - 1]] is None:
                                        if self._board[next_pos] is None:
                                            self._board[curr_pos].set_move_history(next_pos)
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                    else:
                                        return False
                                if position_list[pos - 9] == next_pos and "1" not in curr_pos and "a" not in curr_pos:
                                    if self._board[position_list[pos - 9]] is None:
                                        return False
                                    if self._board[position_list[pos - 9]].get_color() == "WHITE":
                                        self._board[curr_pos].set_move_history(next_pos)
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                    else:
                                        return False
                                if pos < 57:
                                    if position_list[pos + 7] == next_pos and "1" not in curr_pos and "h" not in curr_pos:
                                        if self._board[position_list[pos + 7]] is None:
                                            return False
                                        if self._board[position_list[pos + 7]].get_color() == "WHITE":
                                            self._board[curr_pos].set_move_history(next_pos)
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                            else:
                                return False
                if self._board[curr_pos].label() == "b":
                    for diagonal in diagonal_list:
                        if curr_pos in diagonal and next_pos in diagonal:
                            for index, position in enumerate(diagonal):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "r":
                    for row in rows_list:
                        if curr_pos in row and next_pos in row:
                            for index, position in enumerate(row):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    for column in columns_list:
                        if curr_pos in column and next_pos in column:
                            for index, position in enumerate(column):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "q":
                    for diagonal in diagonal_list:
                        if curr_pos in diagonal and next_pos in diagonal:
                            for index, position in enumerate(diagonal):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[diagonal[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    for row in rows_list:
                        if curr_pos in row and next_pos in row:
                            for index, position in enumerate(row):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[row[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    for column in columns_list:
                        if curr_pos in column and next_pos in column:
                            for index, position in enumerate(column):
                                if position == curr_pos:
                                    curr_num = index
                                if position == next_pos:
                                    next_num = index
                            if curr_num < next_num:
                                for pos in range((curr_num + 1), next_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                            if next_num < curr_num:
                                for pos in range((next_num + 1), curr_num):
                                    if self._board[column[pos]] is None:
                                        continue
                                    else:
                                        return False
                                if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                    self._board[next_pos] = self._board[curr_pos]
                                    self._board[curr_pos] = None
                                    self._turn = "WHITE"
                                    self.check_for_win()
                                    return True
                    else:
                        return False
                if self._board[curr_pos].label() == "n":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if "7" not in curr_pos and "8" not in curr_pos:
                                if "h" not in curr_pos:
                                    if next_pos == position_list[pos + 10]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                if "a" not in curr_pos:
                                    if next_pos == position_list[pos - 6]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                            if "8" not in curr_pos:
                                if "a" not in curr_pos and "b" not in curr_pos:
                                    if next_pos == position_list[pos - 15]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                if "g" not in curr_pos and "h" not in curr_pos:
                                    if next_pos == position_list[pos + 17]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                            if "1" not in curr_pos:
                                if "a" not in curr_pos and "b" not in curr_pos:
                                    if next_pos == position_list[pos - 17]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                if "g" not in curr_pos and "h" not in curr_pos:
                                    if next_pos == position_list[pos + 15]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                            if "1" not in curr_pos and "2" not in curr_pos:
                                if "a" not in curr_pos:
                                    if next_pos == position_list[pos - 10]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                                if "h" not in curr_pos:
                                    if next_pos == position_list[pos + 6]:
                                        if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                            self._board[next_pos] = self._board[curr_pos]
                                            self._board[curr_pos] = None
                                            self._turn = "WHITE"
                                            self.check_for_win()
                                            return True
                    else:
                        return False
                if self._board[curr_pos].label() == "k":
                    for pos in range(0, len(position_list)):
                        if position_list[pos] == curr_pos:
                            if "8" not in curr_pos and "a" not in curr_pos:
                                if next_pos == position_list[pos - 7]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "8" not in curr_pos:
                                if next_pos == position_list[pos + 1]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "8" not in curr_pos and "h" not in curr_pos:
                                if next_pos == position_list[pos + 9]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "a" not in curr_pos:
                                if next_pos == position_list[pos - 8]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "h" not in curr_pos:
                                if next_pos == position_list[pos + 8]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos and "a" not in curr_pos:
                                if next_pos == position_list[pos - 9]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos:
                                if next_pos == position_list[pos - 1]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                            if "1" not in curr_pos and "h" not in curr_pos:
                                if next_pos == position_list[pos + 7]:
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                    else:
                        return False
                if self._board[curr_pos].label() == "h":
                    curr_row = None
                    next_row = None
                    for index, row in enumerate(rows_list):
                        if curr_pos in row:
                            curr_row = index
                        if next_pos in row:
                            next_row = index
                    if curr_row == next_row:
                        return False
                    if curr_row > next_row:
                        for column in columns_list:
                            if curr_pos in column and next_pos in column:
                                for index, position in enumerate(column):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    if curr_row < next_row:
                        for diagonal in diagonal_list:
                            if curr_pos in diagonal and next_pos in diagonal:
                                for index, position in enumerate(diagonal):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    else:
                        return False
                if self._board[curr_pos].label() == "f":
                    curr_row = None
                    next_row = None
                    for index, row in enumerate(rows_list):
                        if curr_pos in row:
                            curr_row = index
                        if next_pos in row:
                            next_row = index
                    if curr_row == next_row:
                        return False
                    if curr_row > next_row:
                        for diagonal in diagonal_list:
                            if curr_pos in diagonal and next_pos in diagonal:
                                for index, position in enumerate(diagonal):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[diagonal[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    if curr_row < next_row:
                        for column in columns_list:
                            if curr_pos in column and next_pos in column:
                                for index, position in enumerate(column):
                                    if position == curr_pos:
                                        curr_num = index
                                    if position == next_pos:
                                        next_num = index
                                if curr_num < next_num:
                                    for pos in range((curr_num + 1), next_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                                if next_num < curr_num:
                                    for pos in range((next_num + 1), curr_num):
                                        if self._board[column[pos]] is None:
                                            continue
                                        else:
                                            return False
                                    if self._board[next_pos] is None or self._board[next_pos].get_color() == "WHITE":
                                        self._board[next_pos] = self._board[curr_pos]
                                        self._board[curr_pos] = None
                                        self._turn = "WHITE"
                                        self.check_for_win()
                                        return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def enter_fairy_piece(self, piece, pos):
        """
        This method will enter a specified fairy piece in a specified position, determined by the passed parameters.
        "H" represents a white hunter, "F" represents a white falcon, "h" represents a black hunter, and "f"
        represents a black falcon. This method will determine whether it is legal to enter the fairy piece, if it's the
        correct turn, correct position, correct piece, if the player has lost enough special pieces, and whether a
        fairy piece of the same type has already been added. If it is a legal move, it initializes the fairy piece and
        adds it to the board and returns True, otherwise is returns False.
        :param piece: The fairy piece being added
        :param pos: Where on the board the fairy piece is to be added
        :return: Returns true if the move is allowed, returns False if the move is illegal.
        """
        white_pieces = []
        black_pieces = []
        for key in self._board:
            if self._board[key] is None:
                continue

            else:
                if self._board[key].get_color() == "WHITE":
                    white_pieces.append(self._board[key].label())

                else:
                    black_pieces.append(self._board[key].label())

        if self._game_state == "UNFINISHED":
            if piece == "H" or piece == "F":
                if self._turn == "BLACK":
                    return False
                if "2" in pos or "1" in pos and self._board[pos] is None:
                    wspecial_piece = 0
                    wfalcon_check = 0
                    whunter_check = 0
                    for wpiece in white_pieces:
                        if wpiece == "R" or wpiece == "N" or wpiece == "B" or wpiece == "Q":
                            wspecial_piece += 1
                        if wpiece == "F":
                            wfalcon_check += 1
                        if wpiece == "H":
                            whunter_check += 1

                    if wspecial_piece < 7:
                        if piece == "H" and whunter_check == 0 and wfalcon_check == 0:
                            whunter = Hunter()
                            whunter.assign_color("WHITE")
                            self._board[pos] = whunter
                            self._turn = "BLACK"
                            return True

                        if piece == "F" and whunter_check == 0 and wfalcon_check == 0:
                            wfalcon = Falcon()
                            wfalcon.assign_color("WHITE")
                            self._board[pos] = wfalcon
                            self._turn = "BLACK"
                            return True

                    if wspecial_piece < 6:
                        if piece == "H" and whunter_check == 0 and wfalcon_check == 1:
                            whunter = Hunter()
                            whunter.assign_color("WHITE")
                            self._board[pos] = whunter
                            self._turn = "BLACK"
                            return True

                        if piece == "F" and whunter_check == 1 and wfalcon_check == 0:
                            wfalcon = Falcon()
                            wfalcon.assign_color("WHITE")
                            self._board[pos] = wfalcon
                            self._turn = "BLACK"
                            return True

                    else:
                        return False
                else:
                    return False
            if piece == "h" or piece == "f":
                if self._turn == "WHITE":
                    return False
                if "7" in pos or "8" in pos and self._board[pos] is None:
                    bspecial_piece = 0
                    bfalcon_check = 0
                    bhunter_check = 0
                    for bpiece in black_pieces:
                        if bpiece == "r" or bpiece == "n" or bpiece == "b" or bpiece == "q":
                            bspecial_piece += 1
                        if bpiece == "f":
                            bfalcon_check += 1
                        if bpiece == "h":
                            bhunter_check += 1

                    if bspecial_piece < 7:
                        if piece == "h" and bhunter_check == 0 and bfalcon_check == 0:
                            bhunter = Hunter()
                            bhunter.assign_color("BLACK")
                            self._board[pos] = bhunter
                            self._turn = "WHITE"
                            return True

                        if piece == "f" and bhunter_check == 0 and bfalcon_check == 0:
                            bfalcon = Falcon()
                            bfalcon.assign_color("BLACK")
                            self._board[pos] = bfalcon
                            self._turn = "WHITE"
                            return True

                    if bspecial_piece < 6:
                        if piece == "h" and bhunter_check == 0 and bfalcon_check == 1:
                            bhunter = Hunter()
                            bhunter.assign_color("BLACK")
                            self._board[pos] = bhunter
                            self._turn = "WHITE"
                            return True

                        if piece == "f" and bhunter_check == 1 and bfalcon_check == 0:
                            bfalcon = Falcon()
                            bfalcon.assign_color("BLACK")
                            self._board[pos] = bfalcon
                            self._turn = "WHITE"
                            return True

                    else:
                        return False
                else:
                    return False

        else:
            return False

    def display_board(self):
        """
        This function builds out a chess board to display in the console. Prints out each position on the board
        private data member using a piece's label or if there is no piece on a position, prints out a space using
        the Space class.
        """
        for key in self._board:
            if self._board[key] is None:
                self._board[key] = Space()

        print("    A   B   C   D   E   F   G   H ")
        print("  +---+---+---+---+---+---+---+---+")
        print("8 | "+self._board["a8"].label()+" | "+self._board["b8"].label()+" | "+self._board["c8"].label()+" | "
              + self._board["d8"].label()+" | "+self._board["e8"].label()+" | "+self._board["f8"].label()+" | "
              + self._board["g8"].label()+" | "+self._board["h8"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("7 | "+self._board["a7"].label()+" | "+self._board["b7"].label()+" | "+self._board["c7"].label()+" | "
              + self._board["d7"].label()+" | "+self._board["e7"].label()+" | "+self._board["f7"].label()+" | "
              + self._board["g7"].label()+" | "+self._board["h7"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("6 | "+self._board["a6"].label()+" | "+self._board["b6"].label()+" | "+self._board["c6"].label()+" | "
              + self._board["d6"].label()+" | "+self._board["e6"].label()+" | "+self._board["f6"].label()+" | "
              + self._board["g6"].label()+" | "+self._board["h6"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("5 | "+self._board["a5"].label()+" | "+self._board["b5"].label()+" | "+self._board["c5"].label()+" | "
              + self._board["d5"].label()+" | "+self._board["e5"].label()+" | "+self._board["f5"].label()+" | "
              + self._board["g5"].label()+" | "+self._board["h5"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("4 | "+self._board["a4"].label()+" | "+self._board["b4"].label()+" | "+self._board["c4"].label()+" | "
              + self._board["d4"].label()+" | "+self._board["e4"].label()+" | "+self._board["f4"].label()+" | "
              + self._board["g4"].label()+" | "+self._board["h4"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("3 | "+self._board["a3"].label()+" | "+self._board["b3"].label()+" | "+self._board["c3"].label()+" | "
              + self._board["d3"].label()+" | "+self._board["e3"].label()+" | "+self._board["f3"].label()+" | "
              + self._board["g3"].label()+" | "+self._board["h3"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("2 | "+self._board["a2"].label()+" | "+self._board["b2"].label()+" | "+self._board["c2"].label()+" | "
              + self._board["d2"].label()+" | "+self._board["e2"].label()+" | "+self._board["f2"].label()+" | "
              + self._board["g2"].label()+" | "+self._board["h2"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("1 | "+self._board["a1"].label()+" | "+self._board["b1"].label()+" | "+self._board["c1"].label()+" | "
              + self._board["d1"].label()+" | "+self._board["e1"].label()+" | "+self._board["f1"].label()+" | "
              + self._board["g1"].label()+" | "+self._board["h1"].label()+" |")
        print("  +---+---+---+---+---+---+---+---+")
        print("    A   B   C   D   E   F   G   H ")

        for key in self._board:
            if self._board[key].label() == " ":
                self._board[key] = None


class Piece:
    """
    This represents a parent Piece class that defines the private data member color and the methods get_color and
    assign_color. These methods return and set the color of any Piece to "WHITE" or "BLACK" in the __init__ of the
    ChessVar class.
    """
    def __init__(self):
        self._color = None

    def get_color(self):
        """
        Returns the private data member color.
        """
        return self._color

    def assign_color(self, color):
        """
        Takes a color parameter and sets the parameter to the private data member color. Will be set to either
        "WHITE" or "BLACK".
        """
        self._color = color


class Pawn(Piece):
    """
    Represents a Pawn chess piece, inheriting from the Piece class. This class adds a move_history private data
    member, to track whether the pawn has moved before for determining whether it is allowed to take a double square
    move. It also has methods to return and set the move history.
    """
    def __init__(self):
        super().__init__()
        self._move_history = None

    def label(self):
        """
        Returns the label of the Pawn piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "P"

        else:
            return "p"

    def get_move_history(self):
        """
        Returns the private data member move_history.
        """
        return self._move_history

    def set_move_history(self, move):
        """
        This method set the private data member to the parameter move. The parameter represents a space on the board.
        """
        self._move_history = move


class Rook(Piece):
    """
    Represents a Rook chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Rook piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "R"

        else:
            return "r"


class Knight(Piece):
    """
    Represents a Knight chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Knight piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "N"

        else:
            return "n"


class Bishop(Piece):
    """
    Represents a Bishop chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Bishop piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "B"

        else:
            return "b"


class Queen(Piece):
    """
    Represents a Queen chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Queen piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "Q"

        else:
            return "q"


class King(Piece):
    """
    Represents a King chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the King piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "K"

        else:
            return "k"


class Hunter(Piece):
    """
    Represents a Hunter chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Hunter piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "H"

        else:
            return "h"


class Falcon(Piece):
    """
    Represents a Falcon chess piece, inheriting from the Piece class.
    """
    def __init__(self):
        super().__init__()

    def label(self):
        """
        Returns the label of the Falcon piece depending on the color private data member.
        """
        if self._color == "WHITE":
            return "F"

        else:
            return "f"


class Space:
    """
    Test class for display board, allows an empty position to be printed as it acts like a Piece class with a label.
    """
    def __init__(self):
        self._space_label = " "

    def label(self):
        """
        Returns the label " " for visualizing the board, provides an empty space
        """
        return self._space_label


def main():
    game = ChessVar()
    # game.display_board()
    game.make_move("c2", "c4")
    game.make_move("d7", "d5")
    game.make_move("c4", "d5")
    game.make_move("e7", "e6")
    game.make_move("b2", "b4")
    game.make_move("e6", "e5")
    game.make_move("d5", "d6")
    game.make_move("e5", "e4")
    game.make_move("d6", "d7")
    game.make_move("e4", "e3")
    # game.make_move("d7", "e8")
    game.make_move("c1", "a3")
    game.make_move("b7", "b6")
    game.make_move("a3", "b2")
    game.make_move("f7", "f6")
    game.make_move("b2", "f6")
    game.make_move("g7", "g5")
    game.make_move("f6", "g5")
    game.make_move("a7", "a5")
    game.make_move("g2", "g3")
    game.make_move("a5", "b4")
    game.make_move("a2", "a4")
    game.make_move("a8", "a5")
    game.make_move("a1", "a3")
    game.make_move("a5", "a4")
    game.make_move("a3", "d3")
    game.make_move("f8", "h6")
    game.make_move("d1", "a4")
    game.make_move("d8", "f6")
    game.make_move("e1", "d1")
    game.make_move("f6", "g5")
    game.enter_fairy_piece("F", "b2")
    game.enter_fairy_piece("f", "e7")
    game.make_move("b2", "a3")
    game.make_move("e7", "f6")
    game.make_move("a3", "a2")
    game.make_move("f6", "f7")
    game.make_move("d7", "e8")
    # game.make_move("b1", "a3")
    # game.make_move("g8", "f6")
    # game.make_move("f8", "b4")
    # game.make_move("g5", "d8")
    # game.enter_fairy_piece("h", "f8")
    # game.make_move("a2", "a4")
    # game.make_move("h7", "h5")
    # game.make_move("d7", "c8")
    # game.make_move("b4", "d2")
    # game.make_move("c8", "c1")
    game.display_board()
    print(game.get_game_state())


if __name__ == "__main__":
    main()
