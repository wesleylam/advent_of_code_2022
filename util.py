def readRaw(inputFile, splitToken = " "):
  lines = []
  with open(inputFile) as f:
    for line in f.readlines():
      # remove new line char
      if line[-1] == '\n':
        line = line[:-1]

      tokens = line.split(splitToken)
      lines.append(tokens)
    return lines