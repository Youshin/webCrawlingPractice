from bs4 import BeautifulSoup


html_str="""
<html>
    <body>
        <ul class='greet'>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class='reply'>
            <li>okay</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = BeautifulSoup(html_str)

ul_reply = bs_obj.find('ul', {'class':'reply'})
print(ul_reply)