import requests

params = {'username':'Ryan', 'password':'password'}

rp = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print(rp.cookies.get_dict())
rp = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=rp.cookies)
print(rp.text)