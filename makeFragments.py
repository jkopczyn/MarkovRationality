import markov
import random
def generateSentence(dictionary):
  sentence = ""
  word = ""
  while word != "\n":
    sentence += " "+word
    word = markov.selectRandomKey(dictionary[word])
  return sentence

def main(num):
  d = markov.readMarkov()
  for i in range(num):
    print generateSentence(d)


main(9)
