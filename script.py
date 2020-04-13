import requests
from bs4 import BeautifulSoup
import pandas as pd




def Corona():
    headers=[]
    t_row=[]
    page =  requests.get('https://www.mohfw.gov.in/')
    bss = BeautifulSoup(page.content,'html.parser')
    head=bss.find('thead')
    table=bss.find('tbody')
    for row in head.findAll('tr'):
        for results in row.text.split('\n'):
            if results=='':
                continue
            else:
                headers.append(results)
    t_row=[rows for rows in table.findAll('tr')]
    state=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in t_row]
    state.pop()
    state.pop()
    return state
print(Corona())
