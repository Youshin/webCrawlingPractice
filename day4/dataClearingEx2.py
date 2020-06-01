from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def clearSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1]
    return sentence

def cleanInput(content):
    content = content.upper()
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    content = content.split('. ')
    content = [word for word in content if word != '']
    return [clearSentence(sentence) for sentence in content]

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)

    return ngrams


html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs_obj = BeautifulSoup(html, 'html.parser')
content = bs_obj.find('div', {'id':'mw-content-text'}).get_text()

ngrams = getNgrams(content,2)
print(ngrams)