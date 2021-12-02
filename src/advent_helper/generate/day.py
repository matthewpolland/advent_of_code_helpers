"""generate the boilerplate for a day.

Usage:
    advent_day [--day=DAY, --name=NAME, --overwrite]
    
"""
import docopt
from .generateday import generateDay
    
if __name__ == '__main__':
    generateDay(docopt.docopt(__doc__))
