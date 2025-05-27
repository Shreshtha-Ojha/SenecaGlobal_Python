# Lambda

def app(fx , value):
  return 6 +fx(value)

square = lambda x: x*x
avg = lambda x,y,z: (x+y+z)/3
print(square(5))              # 25
print(avg(3,5,10))            #6.0
print(app(lambda x: x*2, 2))  #10

# Mapping
def cube(l):
  return l*l*l

l = [1,4,2,6,7,8]
newl = []
newl = list((map(cube,l)))
print(newl)

#Filter
def check(a):
  return a>4
l = [1,4,8,2,0,9,-9]  
newl = list(filter(check,l))  
print(newl)

# Regex
import re

pattern = r"[A-Z]+nglish"
text = '''The English Wikipedia is the primary[a] English -language edition of Wikipedia,
 an online encyclopedia. It was Vnglish created by Jimmy Wales and Larry Sanger on 15 January 
 2001, as Wikipedia's first edition.

English Wikipedia is hosted alongside other language editions by the Wikimedia
 Foundation, an American nonprofit organization. Its content, written independently 
 of other editions by volunteer editors Vnglish known as Wikipedians,[1] is in various 
 varieties of English while aiming to stay consistent within articles. 
 Its internal newspaper is The Signpost.'''

matches = re.finditer(pattern , text)
for match in matches:
  print(match)


''' Output
<re.Match object; span=(4, 11), match='English'>
<re.Match object; span=(40, 47), match='English'>
<re.Match object; span=(112, 119), match='Vnglish'>
<re.Match object; span=(213, 220), match='English'>
<re.Match object; span=(417, 424), match='Vnglish'>
<re.Match object; span=(479, 486), match='English'>'''



