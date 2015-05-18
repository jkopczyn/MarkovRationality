import markov

def addSuccessor(dictionary, prev, succ):
  if not isinstance(dictionary.get(prev), dict):
    dictionary[prev] = {}
  if not dictionary[prev].get(succ):
    dictionary[prev][succ] = 0
  dictionary[prev][succ] += 1
  return dictionary[prev]

def convertCountToLayer(dictionary):
  pass

def createFirstLayer(dictionary, files):
  for aFile in files:
    with open(markov.filepath(aFile)) as page:
      for line in page.readlines():
        prevWord = ""
        for word in line.split():
          addSuccessor(dictionary, prevWord, word)
          prevWord = word
        addSuccessor(dictionary, prevWord, "\n")
  return dictionary

def moreLayers(dictionary):
  pass

def main():
  d = {}
  createFirstLayer(d, markov.files)
  markov.writeMarkov(d)

main()
