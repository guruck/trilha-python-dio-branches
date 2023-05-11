'''modulo para criar um scraper Web'''
import operator
from collections import Counter
import requests
from bs4 import BeautifulSoup


def temperatura():
    '''testando essa biblioteca'''
    site = requests.get('https://www.climatempo.com.br/', timeout=600).content
    soup = BeautifulSoup(site, 'html.parser')
    # print(soup.prettify)
    previsao = soup.find_all('p', class_="-gray _flex _align-center")
    for temp in previsao:
        print(type(temp), temp.get_text(), '\n\n')


def start(url):
    '''inicializa o processo de extracao de palavras de um site'''
    wordlist = []
    source_code = requests.get(url, timeout=600).text

    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    '''limpa a lista de palavras'''
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[|}]\\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    '''cria dicionario das 10 mais'''
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, val in sorted(word_count.items(),
                           key=operator.itemgetter(1)):
        print(f'{key} : {val}')

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    uri = 'https://www.geeksforgeeks.org/'
    api = 'python-programming-language/?ref=leftbar'
    start(uri + api)
