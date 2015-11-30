from datetime import date
from lxml import etree
import urllib2
from nfl_data.nfl_models import NflGame

def fetch_week(year, week, preseason=False):
    """
    Fetch all the games for the specified week
    Note: Data is not available pre-1970
    
    :param year: The season to retrieve data for
    :param week: The week of the season to retrieve data for
    :param preseason: Include preseason? Defaults to False
    :return: Number of games collected
    """
    if week < 1 or week >17:
        raise FetchException('Invalid week')
        
    if year < 1970 or year > date.today().year:
        raise FetchException('Invalid year')
        
    data = urllib2.urlopen(_constructUrlForNFL(year, week))
    results = etree.XML(data.read())
    root = results[0]
    games = {}
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
 
    return len(games)
    
def fetch_season(year, preseason=False):
    """
    Fetch all of the games for a specified season.
    
    Quirky NFL week details:
    < 1970 - Not available on the NFL site
    1970 - 1977 There is 14 weeks to the season
    1978 - 1989 There is 16 weeks to the season (intro of the 16 game season)
    1990 - ? There are 17 weeeks to the season (intro of the bye week)
    
    :param year: The year to retrieve the games for (see rules above)
    :param preseason: Include preseason? Defaults to False
    :return: tuple of (total_weeks, total_games)
    
    """
    total_weeks = 0
    total_games = 0
    for x in range(1, 14):
        total_games += fetch_week(year, x, preseason)
        total_weeks += 1

    if year > 1977:
        total_games += fetch_week(year, 15, preseason)
        total_games += fetch_week(year, 16, preseason)
        total_weeks += 2
    
    if year >= 1990: 
        total_games += fetch_week(year, 17, preseason)
        total_weeks +=1
    
    return total_weeks, total_games
        
def fetch_all_from(start_year, preseason=False):
    pass
    
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

