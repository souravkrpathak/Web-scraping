import urllib.request, urllib.parse, urllib.error
import requests 
from bs4 import BeautifulSoup 
import csv

url = "https://www.passiton.com/inspirational-quotes"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'all_quotes'}) 
  
for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    # quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    # quote['lines'] = row.text 
    quote['lines'] = row.img['alt']
    # quote['author'] = row.p.text 
    quotes.append(quote) 

  
filename = 'quotes.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['url','img','lines']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 
print("CSV file successfully exported !!")