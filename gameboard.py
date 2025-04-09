class GameBoard:
    def __init__(self):
        self.gameboard = """
Square Names
A | B | C
-----------
D | E | F
-----------
G | H | I
Please select a letter EX: 'A' to place your marker there on the board
        """
        self.possible_places = {"A": " ", "B": " ", "C": " ", "D": " ", "E": " ", "F": " ", "G": " ", "H": " ", "I": " "}

    def board(self):
        print(self.gameboard)

    def place_sign(self, move, sign):
        valid_letters = ["A", "B", "C", "D", "F", "E","G", "H", "I"]
        if move not in valid_letters:
            print(f"You typed '{move}' please enter a valid letter.\n")
            return False
        if self.possible_places[f"{move}"] == " ":
            self.possible_places[f"{move}"] = sign
            self.playgameboard = \
                f"""
Play Board
{self.possible_places["A"]} | {self.possible_places["B"]} | {self.possible_places["C"]}
-----------
{self.possible_places["D"]} | {self.possible_places["E"]} | {self.possible_places["F"]}
-----------
{self.possible_places["G"]} | {self.possible_places["H"]} | {self.possible_places["I"]}
Please select a letter EX: 'A' to place your marker there on the board
                    """
            print(self.playgameboard)
            print(self.gameboard)
        else:
            return False

    def checkwin(self, letter):
        wins = [
            ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"],  # Rows
            ["A", "D", "G"], ["B", "E", "H"], ["C", "F", "I"],  # Columns
            ["A", "E", "I"], ["C", "E", "G"]  # Diagonals
        ]
        for combo in wins:
            if all(self.possible_places[pos] == letter for pos in combo):
                print(f"Player {letter} WINS GAME!!")
                return True
        return False
