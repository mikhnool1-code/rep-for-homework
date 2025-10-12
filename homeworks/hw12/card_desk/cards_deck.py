import random


class Card:
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number=None, mast=None):
        self.number = number
        self.mast = mast


class CardsDeck:
    def __init__(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                card = Card(number, mast)
                self.cards.append(card)
        self.cards.append(Card("Joker", "Red"))
        self.cards.append(Card("Joker", "Black"))

    def shuffle(self):
        random.shuffle(self.cards)

    def _card_validator(self, number):
        if not isinstance(number, int):
            raise ValueError("Error: enter a card number from 1 to 54")
        if number < 1 or number > 54:
            raise ValueError("Error: enter a card number from 1 to 54")
        return number

    def get_card(self, number):
        valid_card = self._card_validator(number)
        return self.cards.pop(valid_card - 1)

    def get_remaining_cards(self):
        return self.cards
