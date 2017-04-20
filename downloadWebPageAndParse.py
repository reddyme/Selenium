import requests,bs4
res=requests.get('http://nostarch.com')
res.raise_for_status()
bsOutput=bs4.BeautifulSoup(res.text,"html.parser")
print type(bsOutput)
authorElms=bsOutput.select('#author')
print type(authorElms)
print len(authorElms)
print authorElms[0].getText()
print str(authorElms[0])
print authorElms[0].attrs
