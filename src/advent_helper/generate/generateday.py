from .input import getInput
from datetime import datetime, timezone
from os.path import exists

template = """\
from advent_helper.io import calculateListInput
from advent_helper.problemclass import Problem
from pathlib import Path
import os

class {0}(Problem):
  def partOne(self):
    return

  def partTwo(self):
    return

os.chdir(Path(__file__).parent.parent.absolute())
calculateListInput("input/day{1}.txt", {0}, int)
"""

def writeBoilerplate(name, day):
  
  file = open(f'challenges/day{day}.py', "w") 
  file.writelines(template.format(name, day)) 
  file.close()

def writeInput(day):
  input = getInput(int(day))
  file = open(f'input/day{day}.txt', "w") 
  file.writelines(input)
  file.close()

def generateDay(args):
  day = args['--day'] or datetime.now(timezone.utc).strftime("%d")
  name = args['--name'] or f'Day{day}'
  overwrite = args['--overwrite'] or False

  if exists(f'input/day{day}.txt') and overwrite is False:
    print('These files have already been generated')
    return

  writeBoilerplate(name,day)
  writeInput(day)
