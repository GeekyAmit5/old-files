# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Alleisha.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(6):
    url = tags[17].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

s = tags[17].get('href', None)
pos = s.find("_by_")
end = s.find(".", pos)
print(s[pos+4:end])
