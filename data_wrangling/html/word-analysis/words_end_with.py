
from bs4 import BeautifulSoup
import requests

URL_SEARCH = 'http://todaspalavras.com/ends-with/idade/'

page = requests.get(URL_SEARCH)
soup = BeautifulSoup(page.text, 'html.parser')
lista = soup.find_all('li')
data  = []

print "tamanho da lista inicial: ", len(lista)

for item in lista:
    texto = item.text
    if len(texto) == 10:# print texto, len(texto), texto[3]
        if texto[3] == u'c':
            data.append(texto)

for d in data:
    print '{} {} {}'.format(d, len(d), d[3])


