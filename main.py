import math
import json
from bs4 import beatifulsoup as bsp

def ask():
  #Turn the query into a list 1
  print("Ken: Search Anything")
  query = input("Search: ")
  process = query.translate(str.maketrans('', '',string.punctuation))
  ask = process1.split()
  
def parse():
  #parse results with network() 3
  pass

def search():
  #search wikipedia 2
  url = f'https://en.wikipedia.org/wiki/{subheading}'

  headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
   'Accept-Language': 'en-US,en;q=0.9',
   'Connection': 'keep-alive',
   'Upgrade-Insecure-Requests': '1',
   'Cache-Control': 'max-age=0',
   'Referer': 'https://www.google.com/',
   'Accept-Encoding': 'gzip, deflate, br',
   'DNT': '1',
   'Sec-Fetch-Dest': 'document',
   'Sec-Fetch-Mode': 'navigate',
   'Sec-Fetch-Site': 'cross-site',
   'Sec-Fetch-User': '?1',
   'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A;Brand";v="99"',
   'Sec-Ch-Ua-Mobile': '?0',
   'Sec-Ch-Ua-Platform': '"Windows"',
   'Priority': 'u=0, i'
 }

 try:   #Adjust Next Session
     session = requests.Session()
     response = session.get(url, headers=headers, timeout=10)
     response.raise_for_status()

     soup = BeautifulSoup(response.text, 'html.parser')

     price_element = soup.find('fin-streamer', {'data-symbol': (message), 'data-field': 'regularMarketPrice'})

     change_element = soup.find('fin-streamer', {'data-symbol': (message), 'data-field': 'regularMarketChange'})
     change_percent_element = soup.find('fin-streamer', {'data-symbol': (message), 'data-field': 'regularMarketChangePercent'})

 except exception as e:
   print("Error: {e}")

def construct():
  #construct a response 4
  pass

def network():
  #evaluate encoded data 3a
  pass
