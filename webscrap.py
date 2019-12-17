import urllib.request
page = urllib.request.urlopen("http://www.google.com")
data = (page.read())
print(data)