'''
Tests for the Puzzle class in puzzle.py.

'''

import unittest
import sys
sys.path.append('../scripts/modules')
from puzzle import Puzzle

class TestCaesarCipher(unittest.TestCase):

    # Setup to ensure method is executed correctly
    def setUp(self):
        self.puzzle = Puzzle("username","gender","hair_colour","hat","boots") #no effect on test

    # Test to check if lowercase letters shift correctly
    def test_lower_case_shift(self):
        expected = "bcd"
        actual = self.puzzle.caesar_cipher("abc", 1)
        self.assertEqual(expected, actual, "Should shift lowercase letters")

    # Test to check if uppercase letters shift correctly
    def test_upper_case_shift(self):
        expected = "BCD"
        actual = self.puzzle.caesar_cipher("ABC", 1)
        self.assertEqual(expected, actual, "Should shift uppercase letters")

    # Test to check alphabets wrap around at z
    def test_wrap_around_shift(self):
        expected = "yza"
        actual = self.puzzle.caesar_cipher("xyz", 1)
        self.assertEqual(expected, actual, "Should wrap around end of alphabet")

    # Test to check if cipher effects non-alphabetical characters
    def test_non_alphabetical_characters(self):
        expected = "b.c,d!"
        actual = self.puzzle.caesar_cipher("a.b,c!", 1)
        self.assertEqual(expected, actual, "Should not change non-alphabetic characters")

    # Test to check if cipher effects numbers
    def test_numbers(self):
        expected = "123"
        actual = self.puzzle.caesar_cipher("123", 1)
        self.assertEqual(expected, actual, "Should not change numbers")

    # Test to check if all letters, both capital and lowercase are shifted correctly
    def test_all_letters_shift(self):
        # This test shifts all letters by 1 and checks the result
        all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_shifted = "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA"
        actual = self.puzzle.caesar_cipher(all_letters, 1)
        self.assertEqual(expected_shifted, actual, "Should correctly shift all letters")


if __name__ == "__main__":
    unittest.main()