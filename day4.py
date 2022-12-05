from util import readRaw

def fullyContain(section1Raw, section2Raw):
  t1 = [int(i) for i in section1Raw.split('-')]
  t2 = [int(i) for i in section2Raw.split('-')]
  if t1[0] <= t2[0] and t1[1] >= t2[1]:
    print("yes")
    return True
  return False

def part1(inputFile):
  lines = readRaw(inputFile, splitToken=',')
  score = 0
  for tokens in lines:
    print(tokens)
    if fullyContain(tokens[0], tokens[1]) or \
      fullyContain(tokens[1], tokens[0]):
      score += 1
  return score

if __name__ == "__main__":
  inputFile = 'source/day4.txt'
  print(part1(inputFile))
#   print(part2(inputFile))