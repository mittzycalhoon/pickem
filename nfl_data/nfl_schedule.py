from datetime import date
from lxml import etree
import urllib2
from nfl_data.nfl_models import NflGame

def fetch_week(year, week):
    if week < 1 or week >17:
        raise FetchException('Invalid week')
        
    if year < 1980 or year > date.today().year:
        raise FetchException('Invalid year')
        
    data = urllib2.urlopen(_constructUrlForNFL(year, week))
    results = etree.XML(data.read())
    root = results[0]
    games = {}
    home_wins = 0
    visitor_wins = 0
    for child in root:
        game = NflGame()
        game.eid = child.attrib['eid']
        game.gsis = child.attrib['gsis']
        game.d = child.attrib['d']
        game.t = child.attrib['t']
        game.q = child.attrib['q']
        game.k = child.attrib['k']
        game.h = child.attrib['h']
        game.hnn = child.attrib['hnn']
        game.hs = int(child.attrib['hs'])
        game.v = child.attrib['v']
        game.vnn = child.attrib['vnn']
        game.vs = int(child.attrib['vs'])
        game.p = child.attrib['p']
        game.rz = child.attrib['rz']
        game.ga = child.attrib['ga']
        game.gt = child.attrib['gt']
        games[game.eid] = game
        if game.hs > game.vs:
            home_wins += 1
        else:
            visitor_wins += 1
            
    if home_wins > visitor_wins:
        print 'HOME'
    elif home_wins == visitor_wins:
        print 'TIE'
    else:
        print 'VISITOR'
        
    return ''
    
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

