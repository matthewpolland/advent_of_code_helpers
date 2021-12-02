import requests

session=""
_ga=""

def getInput(day):
  cookies = dict(session=session, _ga=_ga)
  return requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies).text
