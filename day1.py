def part1(inputFile):
  maxCal = 0
  tempCal = 0
  with open(inputFile) as f:
    for line in f.readlines():
      # remove new line char
      if line[-1] == '\n':
        line = line[:-1]

      if line == "":
        # conclude and see if it is the max so far
        if tempCal > maxCal:
          maxCal = tempCal
        # reset  
        tempCal = 0
      else:
        tempCal += int(line)
    
    # for final line 
    if tempCal > maxCal:
      maxCal = tempCal 
    print(maxCal)


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
  inputFile = 'source/day1.txt'
  part1(inputFile)
  part2(inputFile)