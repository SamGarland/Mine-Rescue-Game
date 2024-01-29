'''
Tests for the Leaderboard class in leaderboard.py.

'''
import unittest
import time
import sys
sys.path.append('../scripts/modules')
import leaderboard

class TestLeaderboard(unittest.TestCase):
    
    # Tests for calculating puzzle time.
    # Hypothosis -> if time.per_counter() is the start time and time.perf_counter() is the end time, then
    # the the count_time method in leaderboard.py should calculate time = 0.
    def test_count_time(self):
        CountTime = leaderboard.Leaderboard.count_time(time.perf_counter(),time.perf_counter())
        self.assertEqual(CountTime, 0)
        
if __name__ == "__main__":
    
    unittest.main()