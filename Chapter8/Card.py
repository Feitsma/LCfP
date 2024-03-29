"Paragraph 11.4 of How to Think Like a ComputerScientist: Learning with Python 3Documentation"
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return(self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        """Checks the suits"""
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #if suits are the same -> check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        #tie if also ranks are same
        return 0

    #overloading relational operators
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = " "
        for i in range (len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        #pop function removes last card in list and returns it
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

#Create a deck
red_deck = Deck()
blue_deck = Deck()
