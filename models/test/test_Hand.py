import unittest
from models.Game import Hand, Card

class TestCard(unittest.TestCase):
  def test_instance(self):
    """
    Test instantiation of Hand
    Can hold up to 5 cards - check exception raising
    Cards are the only thing able to go into it - check exception raising
    """

    card1 = Card('A', 'Heart')
    card2 = Card('A', 'Heart')
    card3 = Card('A', 'Heart')
    card4 = Card('A', 'Heart')
    card5 = Card('A', 'Heart')
    card6 = Card('A', 'Heart')

    with self.assertRaises(TypeError):
      hand = Hand(card1, 1)

    with self.assertRaises(SyntaxError):
      hand = Hand(card1, card2, card3, card4, card5, card6)


  def test_add(self):
    """
    Testing the adding of cards


    // exceptions
    Should raise a TypeError when trying to add anything besides a Card + Card

    """

    # this method has to return a Hand
    self.assertEqual(Card('A', 'Heart') + Card('A', 'Heart')+ Card('A', 'Heart'), 13)
    self.assertEqual(Card('A', 'Heart') + Card('Q', 'Heart')+ Card('2', 'Heart'), 13)
    self.assertEqual((Card('A', 'Heart') + Card('Q', 'Heart')+ Card('2', 'Heart') + Card('8', 'Heart')).value, 21)

  def test_indexing(self):
    """
    Testing indexing of hand


    // exceptions
    Should raise a IndexError when trying to index a card that doesn't exist

    """

    card1 = Card('A', 'Heart')
    card2 = Card('3', 'Heart')
    card3 = Card('5', 'Heart')
    card4 = Card('J', 'Heart')
    card5 = Card('A', 'Heart')
    hand = Hand(card1, card2, card3, card4)

    with self.assertRaises(IndexError):
      hand[5]

    hand += card5


    # this method has to return a Hand
    self.assertEqual(hand[1].value, 3)
    self.assertEqual(hand[0].value, 1)
    self.assertEqual(hand[3].value, 10)

if __name__ == '__main__':
    unittest.main(verbosity=1)
