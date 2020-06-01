import requests

session = requests.Session()
params = {'username':'Ryan', 'password':'password'}

rp = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print(rp.cookies.get_dict())
rp = session.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=rp.cookies)
print(rp.text)