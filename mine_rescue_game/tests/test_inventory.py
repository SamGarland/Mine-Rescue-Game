'''
Tests for the Inventory class in inventory.py.

'''
import unittest
import sys

sys.path.append('../scripts/modules')
from inventory import Inventory

# Tests to check if the method correctly identifies players ('test0-3')
# who have specified items
# The Test also checks if the method correctly identifies a player ('test4')
# with the no inventory item
class TestGetInventory(unittest.TestCase):

    def test_inventory_hammer(self):
        puzzle = Inventory("test0")  # Character with hammer
        expected = ['hammer']
        actual = puzzle.get_inventory_item()
        self.assertEqual(expected, actual, "The inventory item should be hammer")

    def test_inventory_lasso(self):
        puzzle = Inventory("test1")  # Character with lasso
        expected = ['lasso']
        actual = puzzle.get_inventory_item()
        self.assertEqual(expected, actual, "The inventory item should be lasso")

    def test_inventory_mask(self):
        puzzle = Inventory("test2")  # Character with mask
        expected = ['mask']
        actual = puzzle.get_inventory_item()
        self.assertEqual(expected, actual, "The inventory item should be mask")

    def test_inventory_notebook(self):
        puzzle = Inventory("test3")  # Character with notebook
        expected = ['notebook']
        actual = puzzle.get_inventory_item()
        self.assertEqual(expected, actual, "The inventory item should be notebook")

    def test_inventory_none(self):
        puzzle = Inventory("test4")  # Character with None as the inventory item
        expected = ['None']
        actual = puzzle.get_inventory_item()
        self.assertEqual(expected, actual, "The inventory item should be None")

# Test to verify if the method correctly identifies that the player ('test0-3')
# has the required items, returning True
# Test to verify if method correctly identifies a player ('test4')
# does not have the required item, returning False
class TestRequiredEquipment(unittest.TestCase):

    def test_character_with_hammer(self):
        # player with hammer
        puzzle = Inventory("test0")
        self.assertTrue(puzzle.has_required_equipment("hammer"),
                        "Should return True when hammer is present")

    def test_character_with_lasso(self):
        # player with lasso
        puzzle = Inventory("test1")
        self.assertTrue(puzzle.has_required_equipment("lasso"),
                        "Should return True when lasso is present")

    def test_character_with_mask(self):
        # player with mask
        puzzle = Inventory("test2")
        self.assertTrue(puzzle.has_required_equipment("mask"),
                        "Should return True when mask is present")

    def test_character_with_notebook(self):
        # player with notebook
        puzzle = Inventory("test3")
        self.assertTrue(puzzle.has_required_equipment("notebook"),
                        "Should return True when notebook is present")

    def test_character_with_none(self):
        # player with 'None'
        puzzle = Inventory("test4")
        self.assertFalse(puzzle.has_required_equipment("notebook"),
                         "Should return False when notebook is not present")

if __name__ == "__main__":
    unittest.main()