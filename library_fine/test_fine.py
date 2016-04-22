
from unittest import TestCase

from datetime import date

from . import fine


class FineTests(TestCase):

    def test_fine_equals_0_when_actual_date_is_before_or_equals_to_expected_date(self):
        expected_date = date(2016, 2, 15)
        actual_date = date(2016, 2, 15)
        hackos = fine.calculate(expected_date, actual_date)
        self.assertEqual(0, hackos)

    def test_fine_equals_255_when_there_is_a_delay_of_17_days(self):
        expected_date = date(2016, 6, 3)
        actual_date = date(2016, 6, 20)
        hackos = fine.calculate(expected_date, actual_date)
        self.assertEqual(255, hackos)

    def test_fine_equals_1000_when_there_is_a_delay_of_2_months(self):
        expected_date = date(2016, 8, 15)
        actual_date = date(2016, 10, 7)
        hackos = fine.calculate(expected_date, actual_date)
        self.assertEqual(1000, hackos)

    def test_fine_equals_10000_when_there_is_a_delay_of_a_year(self):
        expected_date = date(2016, 8, 15)
        actual_date = date(2017, 2, 9)
        hackos = fine.calculate(expected_date, actual_date)
        self.assertEqual(10000, hackos)

    def test_fine_equals_10000_when_there_is_a_delay_greater_than_a_year(self):
        expected_date = date(2016, 8, 15)
        actual_date = date(2019, 1, 19)
        hackos = fine.calculate(expected_date, actual_date)
        self.assertEqual(10000, hackos)
