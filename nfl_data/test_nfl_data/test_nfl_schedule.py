import unittest
from nfl_data.nfl_schedule import fetch_week, FetchException

class TestNflSchedule(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_FetchInvalidWeek(self):
        self.assertRaises(FetchException, fetch_week, 2015, 0)
        
    def test_FetchInvalidYearLow(self):
        self.assertRaises(FetchException, fetch_week, 1979, 1)
        
    def test_FetchInvalidYearHigh(self):
        self.assertRaises(FetchException, fetch_week, 2016, 1)
        
    def test_FetchYearLow(self):
        self.assertEqual(fetch_week(1980, 1), '')
        
    def test_FetchYearHigh(self):
        self.assertEqual(fetch_week(2015, 1), '')
            
    def test_FetchValidWeek(self):
        self.assertEqual(fetch_week(2015, 1), '')
        
