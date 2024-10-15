import os
import random
from colorama import Fore, Style

class Player:                           # denna klass skapar varje spelares nanmn & symbol (dvs. X & O)
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:                             # denna klass hanterar själva spelet, turordningen samt kontrollerar vinnaren
    def __init__(self):
        self.board = [" "] * 9  # tomt spelbräda (3x3)
        self.active_player = None
        self.player1 = None
        self.player2 = None

    def show_board(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")       # detta skapar själva spelbrädan i terminalen


    def control_winner(self):
        winner_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # vinnande kombinationer i rader
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vinnande kombinationer i kolumner
            (0, 4, 8), (2, 4, 6)              # vinnande kombinationer i diagonaler
        ]
        for combination in winner_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return True
        return False

    def tied_game(self):
        return " " not in self.board         # kollar om spelbrädan är fullt

    def play (self):                         # detta är själva spel-loopen
        self.player1 = Player(input("Enter name for player 1: "), Fore.YELLOW + "X" + Style.RESET_ALL)
        self.player2 = Player(input("Enter name for player 2: "), Fore.GREEN + "O" + Style.RESET_ALL)
        self.active_player = self.player1

        while True:
            self.show_board()

            position = self.manage_move()
            self.board[position] = self.active_player.symbol

            if self.control_winner():
                self.show_board()
                print(f"{self.active_player.name} is the winner!")
                self.save_results(f"{self.active_player.name} won!")
                break
            elif self.tied_game():
                self.show_board()
                print("The game is tied.")
                self.save_results("Tied.")
                break

            self.active_player = self.player2 if self.active_player == self.player1 else self.player1
# hello
    def manage_move(self):
        while True:
            try:
                choice = int(input(f"{self.active_player.name} ({self.active_player.symbol}), choose a position (1-9): ")) - 1
                if self.board[choice] == " ":
                    return choice
                else:
                    print("The position is already filled.")
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def save_results(self, results):
        with open("high_scores.txt", "a") as fil:
            fil.write(results + "\n")                     # detta skapar all resultat i en fil så att man kan se de föredetta resultaten. 

if __name__ == "__main__":
    game = Game()
    game.play()

