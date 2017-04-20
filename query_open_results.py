import sys,webbrowser,requests,bs4
if (sys.argv)>1:
    input='+'.join(sys.argv[1:])
source=requests.get('https://www.google.com/search?q='+input)
soupObj=bs4.BeautifulSoup(source.text,"html.parser")
linkElems = soupObj.select('.r a')
#we want to open top 5 results
length=min(5,len(linkElems))
for i in range(length):
    webbrowser.open('http://google.com'+linkElems[i].get('href')) 

