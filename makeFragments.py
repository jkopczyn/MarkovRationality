import json
import random

def readMarkov():
  with open(markovFile, "r") as markov:
    return json.loads(markov.read())

def writeMarkov(d):
  with open(markovFile, "w") as markov:
    markov.write(json.dumps(d))

def selectRandomKey(dictionary):
  reverseLookup = []
  soFar = 0
  for item in a.items():
    reverseLookup.append([item[1]+soFar, item[0]])
    soFar+= item[1]
  choice = random.randint(1,soFar)
  for index in reverseLookup:
    if choice <= index[0]:
      return index[1]

def generateSentence(dictionary)
  sentence = ""
  word = ""
  while word != "\n":
    sentence += " "+word
    word = selectRandomKey(dictionary[word])
  return sentence
