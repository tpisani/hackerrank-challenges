from unittest import TestCase

from . import grid


class GridSearchTests(TestCase):

    def test_grid_search_should_return_true_when_G_contains_P(self):
        match = grid.search(G=["123456",
                               "789123",
                               "456789"],
                            P=["45",
                               "12"])
        self.assertEqual(True, match)

    def test_grid_search_should_return_true_when_G_contains_P_2(self):
        match = grid.search(G=["12345678952679",
                               "68231245232341",
                               "78581625231231",
                               "10957215239912",
                               "83491221213523",
                               "45678911129001"],
                            P=["16252",
                               "72152",
                               "12212"])
        self.assertEqual(True, match)

    def test_grid_search_should_return_false_when_G_does_not_contain_P(self):
        match = grid.search(G=["12345678952679",
                               "68231245232341",
                               "78581625231231",
                               "10957215239912",
                               "83491221213523",
                               "45678911129001"],
                            P=["99999",
                               "99999",
                               "99999",
                               "99999"])
        self.assertEqual(False, match)

    def test_grid_search_should_return_false_when_G_does_not_contain_P_2(self):
        match = grid.search(G=["975899",
                               "185903",
                               "018625"],
                            P=["862",
                               "145"])
        self.assertEqual(False, match)

    def test_grid_search_should_return_false_when_G_contains_P_but_is_not_contiguous(self):
        match = grid.search(G=["7802245812",
                               "9982257530",
                               "0091758994",
                               "1164889635"],
                            P=["175",
                               "116"])
        self.assertEqual(False, match)

    def test_grid_search_should_return_false_when_G_contains_P_but_is_not_contiguous_2(self):
        match = grid.search(G=["3493456107",
                               "5783357208",
                               "1394569906"],
                            P=["578",
                               "906"])
        self.assertEqual(False, match)