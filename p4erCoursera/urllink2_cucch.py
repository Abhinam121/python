# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#from BeautifulSoup import *
from bs4 import *

url = raw_input('Enter - ')
url = "http://www.cucchiaio.it/ricetta/pane-ripieno/?wtk=cpm.newsletter.cuc.2016_01_20&Idtrack=55D69C4304039299A9EA571E779C2850"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
tags = soup('span')
countComments = 0
for tag in tags:
  countComments = countComments + int(tag.contents[0])
   # Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs

print countComments 