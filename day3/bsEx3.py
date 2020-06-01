from bs4 import BeautifulSoup


html_str="""
<html>
    <body>
        <ul class='ko'>
            <li>
                <a href="https://www.naver.com/">네이버</a>
            </li>
            <li>
                <a href="https://www.daum.com/">다음</a>
            </li>
        </ul>
        <ul class='sns'>
            <li>
                <a href="https://www.google.com/">구글</a>
            </li>
            <li>
                <a href="https://www.facebook.com/">페이스북</a>
            </li>
        </ul>
        
    </body>
</html>
"""
bs_obj = BeautifulSoup(html_str, 'html.parser')
atag = bs_obj.find('a')
print(atag['href'])
print(atag.text)

title_list = []
link_list = []

for at in bs_obj.findAll('a'):
    title_list.append(at.text)
    link_list.append(at['href'])

print(title_list)
print(link_list)