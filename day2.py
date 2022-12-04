from util import readRaw

def parseRPS(input):
  # rock
  if input == 'A' or input == 'X':
    return 'Rock'
  # paper
  if input == 'B' or input == 'Y':
    return 'Paper'
  # scissors
  if input == 'C' or input == 'Z':
    return 'Scissor'
  raise Exception("unknown input")

def parse(input):
  # rock
  if input == 'A' or input == 'X':
    return 1
  # paper
  if input == 'B' or input == 'Y':
    return 2
  # scissors
  if input == 'C' or input == 'Z':
    return 3
  raise Exception("unknown input")

def calScore(opponentRaw, youRaw):
  opponent = parse(opponentRaw)
  you = parse(youRaw)

  return calMatchScore(opponent, you) + you

def calMatchScore(opponent, you):
  matchScore = 0
  # win
  if opponent - you == 2: # scissors vs rock
    matchScore = 6
  # lose
  elif opponent - you == -2: # rock vs scissors
    matchScore = 0
  # win
  elif opponent < you:
    matchScore = 6
  # draw 
  elif opponent == you:
    matchScore = 3
  # lose
  elif opponent > you: 
    matchScore = 0
  return matchScore

def part1(inputFile):
  score = 0
  for tokens in readRaw(inputFile):
    assert(len(tokens) == 2)
    score += calScore(tokens[0], tokens[1])
  print(score)
  return score


def parseResult(result):
  # lose
  if result == 'X':
    return 0
  # draw
  if result == 'Y':
    return 3
  # win
  if result == 'Z':
    return 6
  raise Exception("unknown input")
  

def calYou(opponent, result):
  if result == 3: # draw
    return opponent
  elif result == 6: # win
    return ((opponent + 1) % 3) if opponent != 2 else 3
  elif result == 0: # lose
    return (opponent - 1) if opponent != 1 else 3

def calScore2(opponentRaw, resultRaw):
  result = parseResult(resultRaw)
  you  = calYou(parse(opponentRaw), result)
  
  verify = (calMatchScore(parse(opponentRaw), you))
  assert verify == result, (parse(opponentRaw), you, verify, result)
  return result + you
  
def part2(inputFile):
  lines = readRaw(inputFile)
  score = 0
  for tokens in lines:
    temp = calScore2(tokens[0], tokens[1])
    score += temp
  return score

if __name__ == "__main__":
  inputFile = 'source/day2.txt'
  # part1(inputFile)
  print(part2(inputFile))