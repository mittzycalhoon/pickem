import unittest
from fetcher.fetch_functions import fetch 

class TestFetcher(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testFetch(self):
        self.assertTrue(fetch())
        
