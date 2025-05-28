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

match = re.search(pattern, text)
print(match)           

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


#File operations
#open a file
f = open("abc.txt" , "w")
f = open("abc.txt")
f.read()                  #output is an empty string

f = open("abc.txt" , 'w')
f.write("Lorem Ipsum is simply dummy text of the printing \n and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it\n to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including \n versions of Lorem Ipsum.")
f.close()

f = open("abc.txt")
print(f.readline())  #Output only one line
print(f.readlines()) #Output is all the lines as different elements in the list
print(f.read())      #output: The whole paragraph
f.close()
# use of OS module
import os
os.path.exists("abc.txt")
try:
    file = open("newfile.txt", "x")  # Fails if file exists
except FileExistsError:
    print("File already exists")

print(os.path.getsize("abc.txt"))      # Size in bytes   output 581
print(os.path.abspath("abc.txt"))      # Absolute path   output  /content/abc.txt
print(os.path.basename("path/abc.txt"))# File name       output  abc.txt


os.rename('abc.txt', 'newfile.txt')   # Rename file






