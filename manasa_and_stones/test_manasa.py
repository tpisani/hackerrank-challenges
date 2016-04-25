
from unittest import TestCase

from . import manasa


class ManasaTests(TestCase):

    def test_3_stones_for_a_equals_1_and_b_equals_2(self):
        stones = manasa.guess_stones(n=3, a=1, b=2)
        self.assertEqual([2, 3, 4], stones)

    def test_4_stones_for_a_equals_10_and_b_equals_100(self):
        stones = manasa.guess_stones(n=4, a=10, b=100)
        self.assertEqual([30, 120, 210, 300], stones)

    def test_4_stones_for_a_equals_100_and_b_equals_10(self):
        stones = manasa.guess_stones(n=4, a=100, b=10)
        self.assertEqual([30, 120, 210, 300], stones)

    def test_4_stones_for_a_equals_5_and_b_equals_5(self):
        stones = manasa.guess_stones(n=4, a=5, b=5)
        self.assertEqual([15], stones)
