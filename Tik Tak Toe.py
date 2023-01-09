import tkinter as tk
import tkinter.messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        
        # Create the game board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        # Create the buttons
        self.buttons = [[tk.Button(self.window, command=lambda row=i, col=j: self.move(row, col)) for j in range(3)] for i in range(3)]

        # Layout the buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=25, pady=25)

        # Create the reset button
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=1)

        # Create the turn label
        self.turn_label = tk.Label(self.window, text="X's turn", font=("Helvetica", 16))
        self.turn_label.grid(row=3, column=2)

        # Initialize the current player
        self.current_player = 'X'

    def move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            self.check_game_over()
            self.turn_label['text'] = f"{'O' if self.current_player == 'X' else 'X'}'s turn"
            self.toggle_player()

    def check_game_over(self):
        for i in range(3):
            if self.board[i] == ['X', 'X', 'X'] or self.board[i] == ['O', 'O', 'O']:
                self.game_over('X' if self.current_player == 'O' else 'O')
                return

        for i in range(3):
            if self.board[0][i] == 'X' and self.board[1][i] == 'X' and self.board[2][i] == 'X':
                self.game_over('X')
                return
            if self.board[0][i] == 'O' and self.board[1][i] == 'O' and self.board[2][i] == 'O':
                self.game_over('O')
                return

        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            self.game_over('X')
            return
        if self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            self.game_over('O')
            return
        if self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
                        self.game_over('X')
                        return
                    
        if self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
            self.game_over('O')
            return

        # Check for a draw
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            self.game_over(None)
            return

    def game_over(self, winner):
        if winner is None:
            tkinter.messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.turn_label['text'] = f"{self.current_player}'s turn"

    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ' '
                self.buttons[i][j]['state'] = 'normal'
        self.turn_label['text'] = "X's turn"
        self.current_player = 'X'

if __name__ == "__main__":
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()


