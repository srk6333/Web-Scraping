import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import re
fhand = open("html_parser-imagetags.txt",'w')
fhand1 = open("html_parser-linkswith http.txt",'w')

url = "eneter your url"
html = urllib.request.urlopen(url).read() #it give all html code but not parsed
soup = BeautifulSoup(html,'html.parser') #it gives the all html code of the page
tags = soup('img') #give list of all lines which have a tag img
for img in tags:
    fhand.write(str(img))
    fhand.write("\n")
    print(img)
tags = soup('a')
for a in tags:
    print(re.findall('href="(h\S+)',str(a)))
    fhand1.write(str((re.findall('href="(h\S+)',str(a)))))
    fhand1.write("\n")