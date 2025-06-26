# Chess Game Engine

A full-featured chess game engine implemented in Python with advanced chess rules and a command-line interface.

## 🎯 Features

### Core Gameplay
- **Complete Chess Rules**: All standard chess piece movements and rules
- **Move Validation**: Real-time validation of legal chess moves
- **Check Detection**: Automatic detection of check and checkmate situations
- **Game State Management**: Tracks game progress and outcomes

### Advanced Chess Features
- **Castling**: Kingside and queenside castling with proper validation
- **En Passant**: Special pawn capture rule implementation
- **Pawn Promotion**: Automatic promotion when pawns reach the opposite end
- **Move History**: Complete move history with algebraic notation
- **Undo Functionality**: Ability to undo previous moves

### Game End Conditions
- **Checkmate Detection**: Automatic game end when king is checkmated
- **Stalemate Detection**: Draw when no legal moves are available
- **Insufficient Material**: Draw when neither player can win

### User Interface
- **Unicode Chess Symbols**: Beautiful chess piece representation
- **Algebraic Notation**: Standard chess notation (e.g., e2 e4)
- **Move History Display**: Shows all previous moves
- **Interactive Commands**: Support for undo and quit commands

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Run the game:
```bash
python chessn.py
```

## 🎮 How to Play

### Starting the Game
```bash
python chessn.py
```

### Making Moves
- Use algebraic notation: `[from_square] [to_square]`
- Examples:
  - `e2 e4` - Move pawn from e2 to e4
  - `g1 f3` - Move knight from g1 to f3
  - `e1 g1` - Kingside castle (if legal)

### Special Commands
- `undo` - Undo the last move
- `quit` - Exit the game

### Pawn Promotion
When a pawn reaches the opposite end of the board, you'll be prompted to choose a promotion piece:
- `q` - Queen
- `r` - Rook
- `b` - Bishop
- `n` - Knight

## 📋 Game Rules Implemented

### Piece Movements
- **Pawn**: Forward movement, diagonal captures, en passant, two-square initial move
- **Rook**: Horizontal and vertical movement
- **Knight**: L-shaped movement (2+1 squares)
- **Bishop**: Diagonal movement
- **Queen**: Combination of rook and bishop movements
- **King**: One square in any direction, castling

### Special Rules
- **Castling**: King moves two squares toward rook, rook moves to opposite side
- **En Passant**: Pawn captures enemy pawn that just moved two squares
- **Check**: King is under attack
- **Checkmate**: King is in check with no legal moves
- **Stalemate**: No legal moves but king is not in check

## 🏗️ Technical Architecture

### Code Structure
- **Type Annotations**: Full type hints for better code clarity
- **Modular Design**: Separate functions for different game aspects
- **Data Structures**: Lists and dictionaries for board representation
- **Error Handling**: Comprehensive input validation and error messages

### Key Functions
- `create_board()` - Initialize chess board with starting position
- `is_valid_move()` - Validate legal chess moves
- `is_in_check()` - Detect check situations
- `has_legal_moves()` - Check for available legal moves
- `display_board()` - Render board with Unicode symbols

### Data Representation
- **Board**: 8x8 list of lists containing piece dictionaries or None
- **Pieces**: Dictionaries with color, type, and movement status
- **Moves**: Algebraic notation (e.g., "e2 e4")
- **History**: Complete move history with board states

## 🎨 Board Display

The game uses Unicode chess symbols for a clean, professional appearance:

```
  a b c d e f g h
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7
6 . . . . . . . . 6
5 . . . . . . . . 5
4 . . . . . . . . 4
3 . . . . . . . . 3
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1
  a b c d e f g h
```

## 🔧 Development

### File Structure
```
chessn.py          # Main chess game engine
README.md          # This documentation file
```

### Future Enhancements
- [ ] AI opponent with different difficulty levels
- [ ] Save/load game functionality
- [ ] Network multiplayer support
- [ ] GUI interface
- [ ] Opening book integration
- [ ] Move timer/clock
- [ ] Tournament mode

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Acknowledgments

- Unicode chess symbols for beautiful display
- Standard chess notation for move input
- FIDE chess rules for game logic

---

**Enjoy playing chess! ♔♛♖♗♘♙**
