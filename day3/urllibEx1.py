from urllib.request import urlopen

uf = urlopen("http://www.daum.net")
print(uf.read())
print(type(uf))
print('status:', uf.status)
print('content-type:', uf.getheader('Content-Type'))