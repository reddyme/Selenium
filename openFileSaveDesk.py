import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt');
newFile=open('NewFile.txt','wb')
for data in res.iter_content(100000):
    newFile.write(data)
newFile.close()
