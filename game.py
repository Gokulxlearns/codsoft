import tkinter as tk
from tkinter import messagebox

# --- Color and Style Settings ---
BG_COLOR = "#1e1e2f"
BTN_COLOR = "#3b3b4f"
BTN_HOVER = "#505065"
TEXT_COLOR = "#00ffc8"
FONT = ("Courier New", 20, "bold")
TITLE_FONT = ("Helvetica", 24, "bold")

# --- Game Logic ---
def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != '' for row in board for cell in row)

def minimax(board, depth, is_max, alpha, beta):
    if is_winner(board, 'O'):
        return 10 - depth
    elif is_winner(board, 'X'):
        return depth - 10
    elif is_draw(board):
        return 0

    if is_max:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth+1, False, alpha, beta)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth+1, True, alpha, beta)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move():
    best_score = float('-inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def on_click(row, col):
    if board[row][col] == '' and not game_over:
        board[row][col] = 'X'
        buttons[row][col].config(text='X', fg=TEXT_COLOR)
        if is_winner(board, 'X'):
            end_game("You win!")
        elif is_draw(board):
            end_game("It's a draw!")
        else:
            ai_row, ai_col = best_move()
            board[ai_row][ai_col] = 'O'
            buttons[ai_row][ai_col].config(text='O', fg='#ff4d4d')
            if is_winner(board, 'O'):
                end_game("AI wins!")
            elif is_draw(board):
                end_game("It's a draw!")

def end_game(msg):
    global game_over
    game_over = True
    result_label.config(text=msg)


def reset():
    global board, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', bg=BTN_COLOR)
            result_label.config(text='')


def on_enter(e):
    e.widget.config(bg=BTN_HOVER)

def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

# --- GUI Setup ---
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.configure(bg=BG_COLOR)

board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
game_over = False

# Title Label
title = tk.Label(root, text="Tic-Tac-Toe AI", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
title.grid(row=0, column=0, columnspan=3, pady=(10, 20))

# Game Buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text='', width=6, height=3, font=FONT,
                        bg=BTN_COLOR, fg=TEXT_COLOR,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        buttons[i][j] = btn

# Reset Button
reset_btn = tk.Button(root, text='Reset', font=("Arial", 14),
                      bg='#ffcc00', command=reset)
reset_btn.grid(row=4, column=0, columnspan=3, pady=(10, 20))

result_label = tk.Label(root, text='', font=("Arial", 16), fg="#ffcc00", bg=BG_COLOR)
result_label.grid(row=5, column=0, columnspan=3, pady=(5, 10))


root.mainloop()
