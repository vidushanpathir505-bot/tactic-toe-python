import tkinter as tk
import game as gm
from tkinter import messagebox

class GameEngine:

    def __init__(self, root):

        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry('500x550')

        self.bg_color = "#1e1e2f"
        self.btn_color = "#2d2d44"
        self.x_color = "#ff4d4d"
        self.o_color = "#4da6ff"
        self.text_color = "#ffffff"

        self.root.configure(bg=self.bg_color)

        self.game_start()

    def game_start(self):
# This is the openning screen of the app
        self.clear_screen()

        first_screen = tk.Frame(self.root, bg=self.bg_color)

        tk.Label(
            first_screen, 
            text= 'Tic-Tac-Toe',
            font=('Arial', 40, 'bold'), 
            fg=self.text_color,
            bg=self.bg_color
            ).pack(pady=30)

        tk.Button(
            first_screen,
            text='PLAY', 
            font=('Arial', 20),
            bg=self.btn_color,
            fg=self.text_color,
            activebackground='#444',
            relief='flat',
            command=self.playing_mode, 
            padx=20, 
            pady=10
            ).pack(pady=80)

        first_screen.pack(expand=True, fill='both')

    def clear_screen(self):
# clear the widgest in the screen

        for widgest in self.root.winfo_children():
            widgest.destroy()

    def playing_mode(self):
# user choose the playing mode

        self.clear_screen()

        second_screen = tk.Frame(self.root, bg=self.bg_color)

        tk.Label(
            second_screen,
            text="Choose Mode",
            font=('Arial', 28, 'bold'),
            fg=self.text_color,
            bg=self.bg_color
            ).pack(pady=40)


        tk.Button(
            second_screen, 
            text='PVP', 
            font=('Arial', 16, 'bold'), 
            bg=self.btn_color,
            fg=self.text_color,
            activebackground="#444",
            relief="flat",
            command=lambda: self.start_play('pvp'), 
            padx=20, 
            pady=10
            ).pack(pady=20)

        tk.Button(
            second_screen, 
            text='BOT', 
            font=('Arial', 16, 'bold'), 
            command=lambda: self.start_play('bot'),
            bg=self.btn_color,
            fg=self.text_color,
            activebackground="#444",
            relief="flat", 
            padx=20, 
            pady=10
            ).pack(pady=20)

        second_screen.pack(expand=True, fill='both')

    def start_play(self, mode):
# create the game according to the choosen mode

        self.clear_screen()

        if mode == 'pvp':
            self.game = gm.Game('Player 1', 'Player 2', mode='pvp')
        else:
            self.game = gm.Game('Player', None, mode='bot')

        self.game_board()

    def game_board(self):
# creating tic tac toe board using buttons

        third_screen = tk.Frame(self.root)
        self.buttons = []

        for i in range(9): 
            btn = tk.Button(
                third_screen,
                font=('Arial', 24, 'bold'),
                text="",
                width=4,
                height=2,
                bg=self.btn_color,
                fg=self.text_color,
                activebackground='#555',
                relief='flat',
                command=lambda i=i: self.on_button_click(i)
                )

            row = i // 3
            col = i % 3

            btn.grid(row=row, column=col, padx=5, pady=5)

            self.buttons.append(btn)
        
        third_screen.place(relx=0.5, rely=0.5, anchor='center')

    def on_button_click(self, position):
# get the position what user mark

        result = self.game.play_turn(position)

        self.update_board()

        if result == 'Invalid Move':
            return

        if result == 'Continue':
            return
        
        self.show_result(result)

    def show_result(self, result):
#  show result of the game using popup messages

        if "wins" in result:
            message = result
        else:
            message = "It's a Draw!"

        play_again = messagebox.askyesno("Game Over", f"{message}\n\nPlay again?")

        if play_again:
            self.restart_game()
        else:
            self.playing_mode()
        
    def update_board(self):
# get the symbol from the board and update in the board

        for i in range(9):
            value = self.game.board[i]

            if value == '_':
                self.buttons[i].config(text='', state='normal')
            elif value == 'X':
                self.buttons[i].config(text='X', fg=self.x_color, state='disable')
            else:                    
                self.buttons[i].config(text='O', fg=self.o_color, state='disable')

    def restart_game(self):
# restart the game

        self.game.reset_board()

        self.game.current_player = self.game.player1

        self.update_board()


        