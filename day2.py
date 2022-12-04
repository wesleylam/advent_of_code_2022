from enum import Enum

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
    return 0
  # paper
  if input == 'B' or input == 'Y':
    return 1
  # scissors
  if input == 'C' or input == 'Z':
    return 2
  raise Exception("unknown input")

def calScore(opponentRaw, youRaw):
  opponent = parse(opponentRaw)
  you = parse(youRaw)
  print(parseRPS(opponentRaw))
  print(parseRPS(youRaw))

  # win
  if opponent < you or \
    opponent - you == 2: # scissors vs rock
    print("win")
    return 6
  # draw 
  if opponent == you:
    print("draw")
    return 3
  # lose
  if opponent > you or \
    opponent - you == -2: # rock vs scissors
    print("lose")
    return 0

def part1(inputFile):
  score = 0
  with open(inputFile) as f:
    for line in f.readlines():
      # remove new line char
      if line[-1] == '\n':
        line = line[:-1]

      tokens = line.split(" ")
      assert(len(tokens) == 2)
      score += calScore(tokens[0], tokens[1])
      print()
  print(score)
  return score


# pushDownMaxCals(maxCals, 1, 46337)
# [49371, 41171, 33390]
# [49371, 46337, 41171]
def pushDownMaxCals(maxCals, i, newMax):
  maxCals[-1] = -1
  for j in reversed(range(i + 1, len(maxCals))):
    maxCals[j] = maxCals[j-1]
  maxCals[i] = newMax

def part2(inputFile):
  maxCals = [0, 0, 0]
  tempCal = 0
  with open(inputFile) as f:
    for line in f.readlines():
      # remove new line char
      if line[-1] == '\n':
        line = line[:-1]

      if line == "":
        # conclude and see if it can be the top 3 so far
        for i, maxCal in enumerate(maxCals):
          if tempCal > maxCal:
            print(maxCals)
            pushDownMaxCals(maxCals, i, tempCal)
            print(maxCals)
            break
        # reset  
        tempCal = 0
      else:
        tempCal += int(line)
    
    # for final line 
    if tempCal > maxCal:
      maxCal = tempCal 
    print(maxCals)
    print(sum(maxCals))

if __name__ == "__main__":
  inputFile = 'source/day2.txt'
  part1(inputFile)
  # part2(inputFile)