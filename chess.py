# chess_game.py

class Piece:
    def __init__(self, color):
        self.color = color

    def get_symbol(self):
        return "?"

class King(Piece):
    def get_symbol(self):
        return "♔" if self.color == "white" else "♚"

class Queen(Piece):
    def get_symbol(self):
        return "♕" if self.color == "white" else "♛"

class Rook(Piece):
    def get_symbol(self):
        return "♖" if self.color == "white" else "♜"

class Bishop(Piece):
    def get_symbol(self):
        return "♗" if self.color == "white" else "♝"

class Knight(Piece):
    def get_symbol(self):
        return "♘" if self.color == "white" else "♞"

class Pawn(Piece):
    def get_symbol(self):
        return "♙" if self.color == "white" else "♟"

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Place pawns
        for i in range(8):
            self.board[1][i] = Pawn("black")
            self.board[6][i] = Pawn("white")

        # Place major pieces
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(order):
            self.board[0][i] = piece_class("black")
            self.board[7][i] = piece_class("white")

    def display(self):
        print("  a b c d e f g h")
        for i in range(8):
            row = f"{8 - i} "
            for j in range(8):
                piece = self.board[i][j]
                row += piece.get_symbol() if piece else "."
                row += " "
            print(row + f"{8 - i}")
        print("  a b c d e f g h")

if __name__ == "__main__":
    board = Board()
    board.display()

