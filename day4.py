from util import readRaw

def overlap(section1Raw, section2Raw):
  t1 = [int(i) for i in section1Raw.split('-')]
  t2 = [int(i) for i in section2Raw.split('-')]
  if max(t1) >= min(t2) and max(t2) >= min(t1):
    return True
  
  return False

def fullyContain(section1Raw, section2Raw):
  t1 = [int(i) for i in section1Raw.split('-')]
  t2 = [int(i) for i in section2Raw.split('-')]
  if t1[0] <= t2[0] and t1[1] >= t2[1]:
    return True
  return False

def part1(inputFile):
  lines = readRaw(inputFile, splitToken=',')
  score = 0
  for tokens in lines:
    if fullyContain(tokens[0], tokens[1]) or \
      fullyContain(tokens[1], tokens[0]):
      score += 1
  return score

def part2(inputFile):
  lines = readRaw(inputFile, splitToken=',')
  score = 0
  for tokens in lines:
    if overlap(tokens[0], tokens[1]):
      score += 1
  return score

if __name__ == "__main__":
  inputFile = 'source/day4.txt'
  # print(part1(inputFile))
  print(part2(inputFile))