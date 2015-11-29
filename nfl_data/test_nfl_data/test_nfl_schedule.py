import unittest
from nfl_data.nfl_schedule import fetch_week, FetchException

class TestNflSchedule(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_FetchInvalidWeek(self):
        self.assertRaises(Exception, fetch_week, 0)
            
    def test_FetchValidWeek(self):
        self.assertEqual(fetch_week(1), '')
        
