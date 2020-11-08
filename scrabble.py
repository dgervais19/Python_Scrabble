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

    def __init__(self, word):  # Initialize the class
        super().__init__()  # Inherit the attributes from parent class
        self.score = 0  # Set the score to 0 to start off with
        self.word = word.upper()  # .upper() method saves us from having to check if word is capitalised or lower case

    def check_score(self):
        # Create loop that creates a score for the "word" argument that is passed through
        for letter in self.word:
            if letter in self.one:
                self.score += 1
            elif letter in self.two:
                self.score += 2
            elif letter in self.three:
                self.score += 3
            elif letter in self.four:
                self.score += 4
            elif letter in self.five:
                self.score += 5
            elif letter in self.eight:
                self.score += 8
            elif letter in self.ten:
                self.score += 10
            else:
                # Return a logical message if a character isn't in any of the lists
                return "Sorry, one of your letters do not exist, try again "

        return self.score  # Return the score


# Create an object to assign the class to
test = Calculator("Basketball")
print(test.check_score())

