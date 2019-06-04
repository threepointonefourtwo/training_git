from urllib.request import urlopen, Request

response = urlopen(Request('http://www.datacamp.com/teach/documentation'))

print(type(response))

html  = response.read()

print(html)
