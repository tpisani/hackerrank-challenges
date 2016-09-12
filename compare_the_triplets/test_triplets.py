
from unittest import TestCase

from . import triplets


class TripletsTests(TestCase):

    def test_alice_should_have_3_points_and_bob_should_have_0(self):
        A = (3, 5, 6)
        B = (2, 1, 3)
        self.assertEqual(triplets.compare(A, B),
                         (3, 0))

    def test_alice_should_have_2_points_and_bob_should_have_1(self):
        A = (2, 5, 6)
        B = (5, 1, 3)
        self.assertEqual(triplets.compare(A, B),
                         (2, 1))

    def test_alice_should_have_1_point_and_bob_should_have_1(self):
        A = (3, 4, 5)
        B = (3, 2, 6)
        self.assertEqual(triplets.compare(A, B),
                         (1, 1))
