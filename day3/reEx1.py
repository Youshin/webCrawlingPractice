import re
import urllib.request

url = 'https://goo.gl/U7mSQl'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('euckr'))
print(html_contents)

# id_result = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

# print(id_result)