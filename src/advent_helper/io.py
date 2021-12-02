import pyperclip

def _defaultInput(i): return i

def _parseInput(input, handleInput): return [handleInput(i) for i in input.splitlines()]

def _displayAnswer(input, Solutions):
    a, b = Solutions(input).getAnswers()
    pyperclip.copy(b if b else a)

    print("Part one: ", a)
    print("Part two: ", b)

def calculateListInput(filePath, Solutions, handleInput = _defaultInput):
  with open(filePath) as file:
    input = _parseInput(file.read(), handleInput)
    _displayAnswer(input, Solutions)

def calculateBlobInput(filePath, Solutions, handleBlob):
    with open(filePath) as file:
      input = handleBlob(file.read())
      _displayAnswer(input, Solutions)

def poo():
  print('wowa zowa!')