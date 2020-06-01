import re
import urllib.request

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
html = urllib.request.urlopen(url)

html_contents = str(html.read().decode('utf8'))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
# print(url_list)

for url in url_list:
    full_url = ''.join(url)
    file_name = re.findall(r"(ipg)(.+)(zip)", full_url)
    if len(file_name) > 0:
        file_name = ''.join(file_name[0])
        fname, header = urllib.request.urlretrieve(full_url, file_name)
    print("End download")
# print(full_url)