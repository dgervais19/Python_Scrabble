# Create a class named Scrabble
class Scrabble:

    def __init__(self): # initialize the class
        # Define the attributes of the class
        self.one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        self.two = ["D", "G"]
        self.three = ["B", "C", "M", "P"]
        self.four = ["F", "H", "V", "W", "Y"]
        self.five = ["K"]
        self.eight = ["J", "X"]
        self.ten = ["Q", "Z"]


# Create child class called calculator
class Calculator(Scrabble):

    def __init__(self, word): # Initialize the class
        super().__init__()  # Inherit the attributes from parent class

