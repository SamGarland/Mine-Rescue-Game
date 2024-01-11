'''
Tests for the Leaderboard class in leaderboard.py.

'''
import unittest
import time
import sys

sys.path.append('../scripts')
import leaderboard

class TestLeaderboard(unittest.TestCase):
    
    # Tests for calculating puzzle time.
    # Hypothosis -> if time.per_counter() is the start time and time.perf_counter() is the end time, then
    # the the count_time method in leaderboard.py should calculate time = 0.
    def test_count_time(self):
        CountTime = leaderboard.Leaderboard.count_time(time.perf_counter(),time.perf_counter())
        self.assertEqual(CountTime, 0)
    
    # Test to check for username in leaderboard file.
    # Hypothesis -> if the username is not in leaderboard.txt, calling the 
    # method show_leaderboard() will give print statement without the test case.
    def test_show_leaderbord(self):
        username = "Test"
        file_set = []
        with open("../Resources/leaderboard.txt", "r") as lb:
            lines = lb.readlines()
            for line in lines:               
                line = line.strip("\n").split(",")
                file_set.append(line[0])
            self.assertNotIn(username, file_set)
        lb.close()
    
    # Test to check for correct entry into leaderboard.txt.
    # Hypothesis -> if entry is correct, the length of the entry should be 4 and should be greater than the
    # information input in the update_leaderboard() method.
    def test_update_leaderboard(self):
        username = "Test"
        LenUpdate = 3
        leaderboard.Leaderboard(username, "test_puzzle", time.perf_counter()).update_leaderboard()
        with open("../Resources/leaderboard.txt", "r") as lb:
            lines = lb.readlines()
            for line in lines:               
                line = line.strip("\n").split(",")
                if username == line[0]:
                    self.assertGreater(len(line), LenUpdate)
                else:
                    continue
        lb.close()
        
if __name__ == "__main__":
    
    unittest.main(verbosity=3)

