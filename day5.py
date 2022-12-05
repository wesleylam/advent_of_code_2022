from util import readRaw

def parse(inputFile):
  stackDone = False
  stack = None
  commands = []
  lines = readRaw(inputFile, splitToken='')
  for line in lines:
    
    if line == "" or line[0] == " ": # separator line or number line
      # stack define end
      stackDone = True
      continue
    

    # parse stack      
    if not stackDone:
      numStack = int((len(line) + 1) / 4)
      if stack == None:
        # init
        stack = { (j + 1): [] for j in range(numStack) }
        
      for k in range(numStack):
        t = line[k*4:(k*4) + 4]
        crate = t[1]
        if (crate != ' '): stack[k+1].insert(0, crate)      
    else: # parse command
      # "move 21 from 5 to 8"
      t = line.split('move ')[1] # "21 from 5 to 8"
      t = t.split(' from ') # "21" / "5 to 8"
      a = int(t[0])
      t = t[1].split(' to ') # 5/8
      b, c = int(t[0]), int(t[1])
      commands.append((a,b,c))
      
  return stack, commands

def part1(inputFile):
  stack, commands = parse(inputFile)
  for command in commands:
    numToMove, fromCol, toCol = command
    for i in range(numToMove):
      stack[toCol].append(stack[fromCol].pop())
      
  returnStr = ""
  for i, item in stack.items():
    returnStr += (item.pop())
  return returnStr
  

if __name__ == "__main__":
  inputFile = 'source/day5.txt'
  print(part1(inputFile))
  # print(part2(inputFile))