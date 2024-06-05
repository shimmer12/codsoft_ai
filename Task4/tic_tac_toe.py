import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[self.create_button(row, col) for col in range(3)] for row in range(3)]

    def create_button(self, row: int, col: int) -> tk.Button:
        def on_click():
            if self.board[row][col] == ' ' and not self.is_game_over():
                self.board[row][col] = self.current_player
                self.buttons[row][col].config(text=self.current_player)
                if self.check_winner():
                    messagebox.showinfo("Winner", f"{self.current_player} wins!")
                    self.reset_board()
                elif self.is_board_full():
                    messagebox.showinfo("Tie", "It's a tie!")
                    self.reset_board()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'

        button = tk.Button(self.root, text=' ', font=('Arial', 24), width=8, height=4, command=on_click)
        button.grid(row=row, column=col)
        return button

    def check_winner(self) -> bool:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self) -> bool:
        return all(cell != ' ' for row in self.board for cell in row)

    def is_game_over(self) -> bool:
        return self.check_winner() or self.is_board_full()

    def reset_board(self) -> None:
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ' '
                self.buttons[row][col].config(text=' ')
        self.current_player = 'X'

    def run(self) -> None:
        self.root.mainloop()

if __name__ == '__main__':
    game = TicTacToeGUI()
    game.run()
