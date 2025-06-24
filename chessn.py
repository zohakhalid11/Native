# Updated Chess Program Using Lists and Dictionaries
from typing import List, Optional, Any

def get_symbol(piece: Optional[Any]) -> str:
    if not piece:
        return "."
    symbols = {
        "king": {"white": "♔", "black": "♚"},
        "queen": {"white": "♕", "black": "♛"},
        "rook": {"white": "♖", "black": "♜"},
        "bishop": {"white": "♗", "black": "♝"},
        "knight": {"white": "♘", "black": "♞"},
        "pawn": {"white": "♙", "black": "♟"},
    }
    return symbols[piece["type"]][piece["color"]]

def create_piece(color: str, piece_type: str) -> dict:
    return {
        "color": color,
        "type": piece_type,
        "has_moved": False
    }

def create_board() -> List[List[Optional[Any]]]:
    # Define board type to allow both None and piece dictionaries
    board: List[List[Optional[Any]]] = [[None for _ in range(8)] for _ in range(8)]

    # Place pawns
    for i in range(8):
        board[1][i] = create_piece("black", "pawn")
        board[6][i] = create_piece("white", "pawn")

    # Place other pieces
    order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    for i, piece_type in enumerate(order):
        board[0][i] = create_piece("black", piece_type)
        board[7][i] = create_piece("white", piece_type)

    return board

def display_board(board: List[List[Optional[Any]]]) -> None:
    print("  a b c d e f g h")
    for i in range(8):
        row = f"{8 - i} "
        for j in range(8):
            row += get_symbol(board[i][j]) + " "
        print(row + f"{8 - i}")
    print("  a b c d e f g h")

def algebraic_to_index(pos: str) -> tuple[int, int]:
    col = ord(pos[0].lower()) - ord('a')
    row = 8 - int(pos[1])
    return row, col

def main():
    board = create_board()
    current_turn = "white"
    move_history = []

    while True:
        display_board(board)
        move = input(f"{current_turn.capitalize()}'s move (e.g. e2 e4): ").strip()

        if len(move) != 5 or move[2] != ' ':
            print("Invalid format. Use 'e2 e4'. Try again.")
            continue

        start_pos, end_pos = move[:2], move[3:]
        try:
            start_row, start_col = algebraic_to_index(start_pos)
            end_row, end_col = algebraic_to_index(end_pos)
        except:
            print("Invalid positions. Use a-h and 1-8. Try again.")
            continue

        piece = board[start_row][start_col]
        if not piece:
            print("No piece at start position.")
            continue

        if piece["color"] != current_turn:
            print(f"It's {current_turn}'s turn. You can't move {piece['color']} pieces.")
            continue

        # Move piece
        captured = board[end_row][end_col]
        board[end_row][end_col] = piece
        board[start_row][start_col] = None
        piece["has_moved"] = True

        # Save move
        move_history.append({
            "from": (start_row, start_col),
            "to": (end_row, end_col),
            "piece": piece,
            "captured": captured
        })

        # Switch turns
        current_turn = "black" if current_turn == "white" else "white"

if __name__ == "__main__":
    main()