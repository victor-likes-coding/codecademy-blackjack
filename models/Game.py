from .Base import Base

class Card(Base):


  def __init__(self, value, symbol):
    self.face_value = {
      'J': 10,
      'K': 10,
      'Q': 10,
      'A': 11
    }
    if value not in ''.join([str(x) for x in range(2, 10)]) + 'JQKA':
      raise ValueError(f'Parameter `value` was given {value}, can only be 2 - 9, J, Q, K, A')
    super().__init__('Card')
    self.__value = value
    self.__symbol = symbol
    self.__is_face_card = self.__value in self.face_value.keys()
    self.__is_ace_card = self.__value == 'A'


  @property
  def is_face_card(self):
    return self.__is_face_card

  @property
  def is_ace_card(self):
    return self.__is_ace_card

  @property
  def value(self) -> int:
    """ This is a property that returns an int.

    Args:
      None

    Returns:
      The value of the card:
        - 2 - 9 should be 2 - 9
        - JQK = 10
        - A = 11
    """

    return int(self.__value) if not self.is_face_card and not self.is_ace_card else self.face_value[self.__value]

  def __repr__(self):
    return f'Card(value={self.value}, symbol={self.__symbol})'

  def __add__(self, other):
    """
    The math that should be used for adding together 2 cards.

    Args:
      - other: Should be a `<class 'Card'>` object
    """

    if type(other) is Hand:
      print('hello')
      return other + self

    # Check if other is a Card
    if type(other) is not Card:
      raise TypeError(f'Does not support `+` operations using type {type(other)} and type Card. ')
    # 2 cards become a hand
    hand = Hand(self, other)

    # if the hand's value is over 21 and there's an ace in the hand
    if hand.value > 21 and hand.has_ace:
      # pop the ace out of the aces after making it equal to 1
      for index in range(len(hand.aces)):
        card = hand.aces.pop(index)
        card.becomes_one()
        hand.update()
        if hand.value < 21:
          break

    return hand

  def becomes_one(self):
    if self.is_ace_card and self.value == 11:
      self.face_value['A'] = 1


class Hand(Base):
  def __init__(self, *cards: (Card)):
    super().__init__('Hand')
    if not all([type(card) is Card for card in cards]):
      # for card in cards:
        # print(f'Type should be Card, Type: {type(card)}')
      raise TypeError(f'Expected all elements passed into constructor to be of type {type(Card)}')

    if len(cards) > 5:
      raise SyntaxError('Unexpected size of hand cannot exceed 5.')
    self.__cards = [card for card in cards]
    self.__has_ace = any([card.value == 1 or card.value == 11 for card in self.__cards])
    self.__aces = [card for card in self.__cards if card.value == 11]

    self.__value = sum([card.value for card in self.__cards])

    if self.will_require_update():
      self.update_aces()

  @property
  def has_ace(self):
    return self.__has_ace

  @property
  def aces(self):
    return self.__aces

  @property
  def value(self) -> int:
    return self.__value

  def __add__(self, other: Card):
    if type(other) is not Card:
      raise TypeError(f'Does not support `+` operations using type {type(other)} and type {type(self)}. ')

    hand = Hand(*self.__cards, other)

    # if the hand's value is over 21 and there's an ace in the hand
    if hand.will_require_update():
      hand.update_aces()
    return hand

  def __len__(self):
    return len(self.__cards)

  def __iadd__(self, card: Card):
    if not type(card) is Card:
      raise TypeError(f'Cannot add type {type(card)} to type Hand, must be a Card type')

    return Hand(*self.__cards, card)

  def __eq__(self, other: int) -> bool:
    return self.__value == other

  def __iter__(self):
    return self.__cards

  def __getitem__(self, index):
    return self.__cards[index]

  def __repr__(self):
    return f'Hand({[f"{card}" for card in self.__cards]})'

  def update(self) -> None:
    self.__value = sum([card.value for card in self.__cards])

  def will_require_update(self):
      return self.value > 21 and self.has_ace

  def update_aces(self):
    for index in range(len(self.aces)):
      card = self.aces.pop(index)
      card.becomes_one()
      self.update()
      if self.value < 21:
        break
    self.update()