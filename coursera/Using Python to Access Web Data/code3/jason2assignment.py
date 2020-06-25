import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter location: ')
# url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_706995.json"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
# print(json.dumps(js, indent=4))
print(sum([i["count"] for i in js["comments"]]))
