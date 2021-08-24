from enum import Enum

class Card:
    Face = Enum('Face',("A", "two", "three", "four", "5", "6", "7", "8", "9", "10", "J", "Q", "K"))
    Suit = Enum('Suit',('Diamonds', "Clubs", "Spades", "Hearts"))

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face.name}, {self.suit.name})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()

    def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()
            
    def __add__(self, other):
        return self.getValue() + other.getValue()

    def getValue(self):
        picture = {'A':1, 'J':11, 'Q':12, 'K':13}
        if self.face.name.isdigit():
            return int(self.face.name)
        return picture[self.face.name]


if __name__ == '__main__':
    heartsJ = Card(Card.Face.J, Card.Suit.Hearts)
    print(heartsJ)
    print(heartsJ.getValue())

    diamondsJ = Card(Card.Face.J, Card.Suit.Diamonds)
    print(diamondsJ)
    print(diamondsJ.getValue())

    clubsK = Card(Card.Face.K, Card.Suit.Clubs)

    print(heartsJ==diamondsJ)
    print(clubsK>heartsJ)
    print(clubsK<heartsJ)
    print(heartsJ+diamondsJ)

    