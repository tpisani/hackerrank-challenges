
from unittest import TestCase

from . import cavity_map


class CavityMapTests(TestCase):

    def test_cavities_1(self):
        C = cavity_map.cavities([[1, 1, 1, 2],
                                 [1, 9, 1, 2],
                                 [1, 8, 9, 2],
                                 [1, 2, 3, 4]])
        self.assertEqual([[1, 1],
                          [2, 2]],
                         C)

    def test_cavities_2(self):
        C = cavity_map.cavities([[0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 9, 0, 0],
                                 [0, 0, 0, 0, 0, 0],
                                 [0, 0, 9, 9, 0, 0],
                                 [0, 9, 0, 0, 9, 0],
                                 [0, 0, 0, 9, 0, 0]])
        self.assertEqual([[1, 3],
                          [4, 1],
                          [4, 4]],
                         C)
