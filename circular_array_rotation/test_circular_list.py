
from unittest import TestCase

from . import circular_list


class CircularArrayRotationTests(TestCase):
    sample_list = [8, 4, 6, 9, 1, 2]

    def test_rotate_1_time(self):
        rotated = circular_list.rotate(self.sample_list, 1)
        self.assertEqual(rotated[0], 2)

    def test_rotate_3_times(self):
        rotated = circular_list.rotate(self.sample_list, 3)
        self.assertEqual(rotated[2], 2)

    def test_rotate_10_times(self):
        rotated = circular_list.rotate(self.sample_list, 10)
        self.assertEqual(rotated[3], 2)
