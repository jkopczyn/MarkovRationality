import urllib2
import re
from HTMLParser import HTMLParser

prefix = "http://slatestarcodex.com/20"
filepath = "sources/"

posts = [["13/07/17/","who-by-very-slow-decay/"
], ["14/02/23/", "in-favor-of-niceness-community-and-civilization/",
], ["14/07/30/", "meditations-on-moloch/", 
], ["13/09/12/", "the-life-cycle-of-medical-ideas/",
], ["13/09/28/", "sleep-now-by-prescription/", 
], ["14/06/15/", "fish-now-by-prescription/",
], ["14/08/16/", "an-iron-curtain-has-descended-upon-psychopharmacology/",
], ["14/05/06/", "evening-doc/"
], ["14/06/30/", "medicine-as-not-seen-on-tv/"
], ["14/08/16/", "burdens/"
], ["14/04/28/", "the-control-group-is-out-of-control/",
], ["13/12/17/", "statistical-literacy-among-doctors-now-lower-than-chance/",
], ["14/01/02/", "two-dark-side-statistics-papers/",
], ["13/08/29/", "fake-euthanasia-statistics/", 
], ["13/05/22/", "the-wisdom-of-the-ancients/",
], ["14/04/26/", "stop-confounding-yourself-stop-confounding-yourself/",
], ["13/03/04/", "a-thrivesurvive-theory-of-the-political-spectrum/",
], ["13/12/08/", "a-something-sort-of-like-left-libertarianism-ist-manifesto/",
], ["13/12/29/", "the-spirit-of-the-first-amendment/",
], ["14/04/22/", "right-is-the-new-left/",
], ["14/03/08/", "the-slate-star-codex-political-spectrum-quiz/",
], ["13/04/20/", "social-justice-for-the-highly-demanding-of-rigor/",
], ["14/01/12/", "a-response-to-apophemi-on-triggers/", 
], ["14/06/14/", "living-by-the-sword/",
], ["14/07/07/", "social-justice-and-words-words-words/",
], ["13/06/22/", "social-psychology-is-a-flamethrower/",
], ["14/05/30/", "the-wonderful-thing-about-triggers/",
], ["14/01/05/", "marijuana-much-more-than-you-wanted-to-know/",
], ["14/03/30/", "wheat-much-more-than-you-wanted-to-know/",
], ["14/07/07/", "ssris-much-more-than-you-wanted-to-know/",
], ["13/06/13/", "arguments-from-my-opponent-believes-something/",
], ["13/06/09/", "all-debates-are-bravery-debates/",
], ["14/05/12/", "weak-men-are-superweapons/",
], ["13/05/02/", "if-its-worth-doing-its-worth-doing-with-made-up-statistics/",
], ["14/08/14/", "beware-isolated-demands-for-rigor/", 
], ["13/04/06/", "polyamory-is-boring/",
], ["13/06/30/", "the-lottery-of-fascinations/", 
], ["13/11/19/", "genetic-russian-roulette/",
], ["14/03/17/", 
"what-universal-human-experiences-are-you-missing-without-realizing-it/"]]

headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

class ParagraphParser(HTMLParser):
  def __init__(self, file):
    self.file = file
    self.enclosing_ps = 0
  def handle_starttag(self, tag, attrs):
    if tag == "p":
      self.enclosing_ps += 1
  def handle_endtag(self, tag):
    if tag == "p":
      self.enclosing_ps -= 1
  def handle_data(self, data):
    if self.enclosing_ps >= 1:
      self.file.write(data + "\n")
    print("Encountered some data  :", data)

for post in posts:
  try:
    print post[0]
    print post[1]
    response = urllib2.urlopen(urllib2.Request(prefix+post[0]+post[1], "", headers))
  except urllib2.HTTPError as e:
    print e.geturl()
    print e.read()
  with open(filepath+post[1].rstrip('/')+".html", 'w+') as localHTML:
    localHTML.write(response.read());

for post in posts:
  with open(filepath+post[1].rstrip('/')+".html", 'r') as localHTML:
    htmlLines = localHTML.readlines()
    with open(filepath+post[1].rstrip('/')+".txt", 'w+') as textFile:
      for line in htmlLines:
        title = re.search(r'(?<=<h1 class="pjgm-posttitle">).*(?=</h1>)', line)
        if title:
          textFile.write(title.group(0)+"\n")
          break
