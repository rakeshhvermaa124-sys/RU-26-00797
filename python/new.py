def display_board(board):
    """Prints the current state of the 3x3 board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_win(board):
    """
    Checks all 8 winning lines (3 rows, 3 columns, 2 diagonals).
    Returns a tuple (True, winning_line_string) if someone wins, otherwise (False, "").
    """
    
    winning_combinations = [
        (0, 1, 2, "1-2-3"),  
        (3, 4, 5, "4-5-6"),  
        (6, 7, 8, "7-8-9"),  
        (0, 3, 6, "1-4-7"),  
        (1, 4, 7, "2-5-8"),  
        (2, 5, 8, "3-6-9"),  
        (0, 4, 8, "1-5-9"),  
        (2, 4, 6, "3-5-7")   
    ]
    
    for a, b, c, line_name in winning_combinations:
        if board[a] == board[b] == board[c]:
            return True, line_name
            
    return False, ""


def check_draw(move_count):
    """Checks if the board is full (9 moves reached)."""
    if move_count == 9:
        return True
    return False


def play_game():
    """Main function to run a single game of Tic-Tac-Toe."""
    
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"  
    move_count = 0
    game_over = False

    print("--- Welcome to Tic-Tac-Toe ---")
    display_board(board)

    while not game_over:
        
        user_input = input(f"Player {current_player}, enter your move (1-9): ").strip()

        
        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 9:
            print("Invalid position. Enter a number from 1 to 9.")
            continue  
        position = int(user_input)
        index = position - 1  

        
        if board[index] == "X" or board[index] == "O":
            print(f"Position {position} is already taken. Choose another position.")
            continue 
        
        board[index] = current_player
        move_count += 1
        display_board(board)

        
        is_win, winning_line = check_win(board)
        if is_win:
            print(f"Player {current_player} wins!")
            print(f"Winning line: {winning_line}")
            game_over = True
            break

        
        if check_draw(move_count):
            print("Board is full after 9 moves.")
            print("It's a draw! No moves left.")
            game_over = True
            break

        
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


 
if __name__ == "__main__":
    while True:
        play_game()
        
         
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break