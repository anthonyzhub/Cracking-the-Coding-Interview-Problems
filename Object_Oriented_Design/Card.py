# Cracking the Coding Interview - pp. 127 - q 7.1

class Card:

    def __init__(self, name, color, value) -> None:
        self.name = name
        self.color = color
        self.value = value

class AdvancedCard:

    def setSuit(self, suit):

        # OBJECTIVE: Set card's suit based on "suit" variable

        if suit in {"Clubs", "Hearts", "Spades", "Diamonds"}:
            self.suit = suit

    def setName(self, name):

        # OBJECTIVE: Set card name based on "name" variable

        # If name is in set, set name variable
        if name in {"Jack", "Queen", "King", "Ace"}:
            self.name = name

        # If name is numeric only, set name variable
        elif name.isnumeric():
            self.name = name

        # If all above conditions are false, set card as invalid
        else:
            self.name = "INVALID CARD!"

    def setColor(self):

        # OBJECTIVE: Set card's color based on suit type

        if self.suit == "Clubs" or self.suit == "Spades":
            self.color = "Black"

        elif self.suit == "Hearts" or self.suit == "Diamonds":
            self.color = "Red"

    def setValue(self, value):

        # OBJECTIVE: Set card's color based on card's name

        if self.name == "Jack":
            self.value = 11
        
        elif self.name == "Queen":
            self.value = 12
        
        elif self.name == "King":
            self.value = 13

        elif self.name == "Ace":

            # If card's name is Ace and input "value" is either 1 or 11, set it as input.
            # If an invalid value was given (e.g., 13), set card's value to 1 as default
            self.value = value if value == 1 or value == 11 else 1

        # Change "name" to an integer. NOTE: In setName(), if "name" is numeric, integer conversion won't throw an error
        elif self.name.isnumeric():
            tmpValue = int(self.name)

            if tmpValue > 1 and tmpValue < 10:
                self.value = tmpValue
            else:
                self.value = -1

    def __init__(self, suit, name, value=0):

        self.setSuit(suit)
        self.setName(name)
        self.setColor()
        self.setValue(value)

    def info(self):
        print("{} {} {} {}".format(self.color, self.suit, self.name, self.value))

def main():

    one = AdvancedCard("Clubs", "King")
    two = AdvancedCard("Hearts", "Jack")
    three = AdvancedCard("Spades", "Queen")
    four = AdvancedCard("Diamonds", "Ace")
    five = AdvancedCard("Hearts", "1")

    one.info()
    two.info()
    three.info()
    four.info()
    five.info()

main()