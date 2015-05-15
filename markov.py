import json

files = [ "Rationality_From_AI_to_Zombies",
"who-by-very-slow-decay",
"in-favor-of-niceness-community-and-civilization",
"meditations-on-moloch", 
"the-life-cycle-of-medical-ideas",
"sleep-now-by-prescription", 
"fish-now-by-prescription",
"an-iron-curtain-has-descended-upon-psychopharmacology",
"evening-doc",
"medicine-as-not-seen-on-tv",
"burdens",
"the-control-group-is-out-of-control",
"statistical-literacy-among-doctors-now-lower-than-chance",
"two-dark-side-statistics-papers",
"fake-euthanasia-statistics", 
"the-wisdom-of-the-ancients",
"stop-confounding-yourself-stop-confounding-yourself",
"a-thrivesurvive-theory-of-the-political-spectrum",
"a-something-sort-of-like-left-libertarianism-ist-manifesto",
"the-spirit-of-the-first-amendment",
"right-is-the-new-left",
"the-slate-star-codex-political-spectrum-quiz",
"social-justice-for-the-highly-demanding-of-rigor",
"a-response-to-apophemi-on-triggers", 
"living-by-the-sword",
"social-justice-and-words-words-words",
"social-psychology-is-a-flamethrower",
"the-wonderful-thing-about-triggers",
"marijuana-much-more-than-you-wanted-to-know",
"wheat-much-more-than-you-wanted-to-know",
"ssris-much-more-than-you-wanted-to-know",
"arguments-from-my-opponent-believes-something",
"all-debates-are-bravery-debates",
"weak-men-are-superweapons",
"if-its-worth-doing-its-worth-doing-with-made-up-statistics",
"beware-isolated-demands-for-rigor", 
"polyamory-is-boring",
"the-lottery-of-fascinations", 
"genetic-russian-roulette",
"what-universal-human-experiences-are-you-missing-without-realizing-it"]

markovFile = "db.txt"

def filepath(aFile):
  return "sources/"+aFile+".txt"

def readMarkov():
  with open(markovFile, "r") as markov:
    return json.loads(markov.read())

def writeMarkov(d):
  with open(markovFile, "w") as markov:
    markov.write(json.dumps(d, separators=(',',':')))

def addSuccessor(dictionary, prev, succ):
  if not isinstance(dictionary.get(prev), dict):
    dictionary[prev] = {}
  if not dictionary[prev].get(succ):
    dictionary[prev][succ] = 0
  dictionary[prev][succ] += 1
  return dictionary[prev]

def convertCountToLayer(dictionary):
  pass

def createFirstLayer(dictionary):
  for aFile in files:
    with open(filepath(aFile)) as page:
      for line in page.readlines():
        prevWord = ""
        for word in line.split():
          addSuccessor(dictionary, prevWord, word)
          prevWord = word
  return dictionary

def moreLayers(dictionary):
  pass






def main():
  d = readMarkov()
  createFirstLayer(d)
  writeMarkov(d)

main()
