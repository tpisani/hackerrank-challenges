
from unittest import TestCase

from . import cavity_map


class CavityMapTests(TestCase):

    def test_cavities_should_return(self):
        C = cavity_map.cavities([[1, 1, 1, 2],
                                 [1, 9, 1, 2],
                                 [1, 8, 9, 2],
                                 [1, 2, 3, 4]])
        self.assertEqual([[1, 1],
                          [2, 2]],
                         C)
