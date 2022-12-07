from util import readRaw

def part1(inputFile, k = 4):
  lines = readRaw(inputFile, splitToken='')
  line = lines[0]
  for i in range(len(line)): 
    if len(set(line[i:i+k])) == k: return i + k
    
  return

def part2(inputFile):
  return part1(inputFile, 14)
  
if __name__ == "__main__":
  inputFile = 'source/day6.txt'
  # print(part1(inputFile))
  print(part2(inputFile))