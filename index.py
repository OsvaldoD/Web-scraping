import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.bci.co.mz/Canais/Cotacoes.asp?Id=774')
soup = BeautifulSoup(page.content, 'html.parser')

date = soup.find('b').get_text()
title = soup.find('p').get_text()
table = soup.find('table')

counter = 1
countries, moeda, compra ,venda = ([] for i in range(4))

table_head = table.find('th')
table_body = table.find('tbody')

table_header = table_body.find_all('th')
clean_headers = [data.get_text() for data in table_header]

table_data = table_body.find_all('tr')
clean_data = [data.find_all('td') for data in table_data]
clean_data.pop(0)

while counter <= len(clean_data)-1:
    countries.append(clean_data[counter][0].get_text())
    moeda.append(clean_data[counter][1].get_text())
    compra.append(clean_data[counter][2].get_text())
    venda.append(clean_data[counter][3].get_text())
    counter = counter + 1
       

table_of_data = pd.DataFrame({
    clean_headers[0]: countries,
    clean_headers[1]: moeda,
    clean_headers[2]: compra,
    clean_headers[3]: venda
})

print('\t \t', title)
print('\t', table_head.get_text())
print(' ', date, '\n')
print('\t',table_of_data)






