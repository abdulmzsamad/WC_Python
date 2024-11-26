# tests/test_wc.py
import sys
print(sys.path)

import os
import unittest
from wc.wc import WC

class TestWC(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'resources/text.txt'
        self.wc = WC(self.test_filename)
        self.wc.calculate_stats()

    # def tearDown(self):

    def test_bytes(self):
        self.assertEqual(self.wc.bytes, 342190)

    def test_lines(self):
        self.assertEqual(self.wc.lines, 7145)

    def test_words(self):
        self.assertEqual(self.wc.words, 58164)

    def test_characters(self):
        self.assertEqual(self.wc.characters, 339292)

if __name__ == "__main__":
    unittest.main()
