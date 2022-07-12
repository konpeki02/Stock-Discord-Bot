import unittest
from src import bot


class TestBot(unittest.TestCase):
    def test_getKey(self):
        self.assertEqual(bot.getKey('agent.json', 'KEY'), 'TEST_KEY_VALUE')


if __name__ == 'main':
    unittest.main()
