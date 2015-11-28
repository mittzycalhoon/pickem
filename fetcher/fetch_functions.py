import urllib2
from lxml import etree

def fetch_week(week):
    if week < 1 or week >17:
        raise FetchException('Invalid week')
        
    data = urllib2.urlopen(_constructUrlForNFL(2015, week))
    results = etree.XML(data.read())
    root = results[0]
    for child in root:
        print ('%s %s vs. %s %s' % (child.attrib['hnn'], child.attrib['hs'], child.attrib['vnn'], child.attrib['vs']))
    return True
    
def _constructUrlForNFL(year, week, preseason=False):
    type = 'REG'
    if preseason:
        type = 'PRE'
        
    url = 'http://www.nfl.com/ajax/scorestrip?season=%d&seasonType=%s&week=%d' % (year, type, week)
    return url

class FetchException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

