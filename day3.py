from util import readRaw

def findDup(c1, c2):
  s = set(c1)
  dup = set()
  for c in c2: 
    if c in s:
      # dup.add(c)
      return c
  raise Exception("cant find dup")

def toPrior(dup):
  if (dup == dup.lower()):
    return ord(dup) - 96
  else:
    return ord(dup) - 38


def calPrior(c1, c2):
  dup = findDup(c1, c2)
  return toPrior(dup)

def part1(inputFile):
  lines = readRaw(inputFile)
  score = 0
  for tokens in lines:
    rucksack = tokens[0]
    half = int(len(rucksack) / 2)
    containers = (rucksack[:half], rucksack[half:])
    # print(containers[0])
    # print(containers[1])
    
    temp = calPrior(containers[0], containers[1])
    score += temp
  return score

if __name__ == "__main__":
  inputFile = 'source/day3.txt'
  print(part1(inputFile))