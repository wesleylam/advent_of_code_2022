from util import readRaw

def getDirSizes(inputFile):
  lines = readRaw(inputFile, splitToken=' ')
  
  levels = {}
  levelFlag = -1
  pwd = ""
  store = {}
  looking = None
  for tokens in lines:
    if tokens[0] == "$" and tokens[1] == "ls": # ignore
      continue
    
    if tokens[0] == "$" and tokens[1] == "cd": # command line 
      d = tokens[2]
      
      if d == "..": # ignore "cd .."
        levelFlag -= 1
        pwd = "/".join(pwd.split("/")[:-1])
        if pwd == "": pwd = "/"
        continue 
      levelFlag += 1
      # update pwd except the first one (root)
      if d != "/": 
        pwd += ("/" + d) if pwd != "/" else d
      else:
        pwd = "/"
      
      looking = pwd
      if pwd not in store:
        store[pwd] = []
      if levelFlag not in levels:
        levels[levelFlag] = []
      levels[levelFlag].append(pwd)
      continue
    
    # below must be result of ls
    size, d = tokens[0], tokens[1]
    store[looking].append(int(size) if size != "dir" else d)
    
  
  finalSizes = {} 
  
  # print(store)
  # print(levels)
  for i in reversed(range(len(levels))):
    levelList = levels[i]
    for path in levelList:
      temp = 0
      for size in store[path]:
        print(i, path, size)
        if type(size) != int: 
          toPath = (path + "/" + size) if path != "/" else "/" + size
          size = finalSizes[toPath] 
        temp += size
      finalSizes[path] = temp
      
  return finalSizes

def part1(inputFile):
  finalSizes = getDirSizes(inputFile)
    
  # print(finalSizes)
  return sum([size for p, size in finalSizes.items() if size <= 100000])


def part2(inputFile):
  finalSizes = getDirSizes(inputFile)
  totalSpace = 70000000
  freeSpace = totalSpace - finalSizes["/"]
  requireSpace = 30000000
  
  least = totalSpace
  for p, size in finalSizes.items():
    if size + freeSpace >= requireSpace:
      least = size if size < least else least
  return least
  
if __name__ == "__main__":
  inputFile = 'source/day7.txt'
  # print(part1(inputFile))
  print(part2(inputFile))