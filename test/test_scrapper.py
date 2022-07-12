import unittest
from src import scrapper


class TestScrapper(unittest.TestCase):
    def test_parser(self):
        price = '3,875.50-25.75 (-0.66%)As of  01:21PM EDT. Market open.'
        self.assertEqual(scrapper.get_price(price), '3,875.50')
        self.assertEqual(scrapper.get_change(price), '-25.75 ')
        self.assertEqual(scrapper.get_percent_change(price), '(-0.66%')
        self.assertEqual(scrapper.get_just_quote(price), '3,875.50-25.75 (-0.66%)')


if __name__ == 'main':
    unittest.main(verbosity=2)
