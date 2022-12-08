import unittest
from models.Game import Card

class TestCard(unittest.TestCase):
  def testValue(self):
    """
    Testing the value of a Card
    2 - 9 should be 0 - 9
    J, Q, K should be 10
    A should be 11
    10+ should be rejected
    """

    self.assertEqual(Card('2', 'Heart').value, 2)
    self.assertEqual(Card('9', 'Heart').value, 9)
    self.assertEqual(Card('J', 'Heart').value, 10)
    self.assertEqual(Card('Q', 'Heart').value, 10)
    self.assertEqual(Card('K', 'Heart').value, 10)
    self.assertEqual(Card('A', 'Heart').value, 11)
    self.assertRaises(ValueError, Card, value='10', symbol='Heart')
    self.assertRaises(ValueError, Card, value='999', symbol='Heart')
    self.assertRaises(ValueError, Card, value='1', symbol='Heart')

  def test_add(self):
    """
    Testing the adding of cards
    Card('A', 'Heart') + Card(9, 'Heart'), 20
    Card('A', 'Heart') + Card('J', 'Heart'), 21
    Card('A', 'Heart') + Card('Q', 'Heart'), 21
    Card('A', 'Heart') + Card('K', 'Heart'), 21
    Card('A', 'Heart') + Card('A', 'Heart'), 12
    Card('2', 'Heart') + Card('3', 'Heart'), 5
    Card('7', 'Heart') + Card('8', 'Heart'), 15

    // exceptions
    Should raise a TypeError when trying to add anything besides a Card + Card

    """
    with self.assertRaises(TypeError):
      Card('A', 'Heart') + 5

    self.assertEqual(Card('A', 'Heart') + Card('9', 'Heart'), 20)
    self.assertEqual(Card('A', 'Heart') + Card('J', 'Heart'), 21)
    self.assertEqual(Card('A', 'Heart') + Card('Q', 'Heart'), 21)
    self.assertEqual(Card('A', 'Heart') + Card('K', 'Heart'), 21)
    self.assertEqual(Card('A', 'Heart') + Card('A', 'Heart'), 12)
    # this method has to return a Hand
    # self.assertEqual(Card('A', 'Heart') + Card('A', 'Heart')+ Card('A', 'Heart'), 13)
    self.assertEqual(Card('2', 'Heart') + Card('3', 'Heart'), 5)
    self.assertEqual(Card('7', 'Heart') + Card('8', 'Heart'), 15)

if __name__ == '__main__':
    unittest.main(verbosity=1)
