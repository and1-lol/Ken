import math
import json
from bs4 import BeautifulSoup
import requests
import string

letters = {
  " ": 41
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
  "e": 5,
  "f": 6, 
  "g": 7,
  "h": 8,
  "i": 9,
  "j": 10,
  "k": 11,
  "l": 12,
  "m": 13,
  "n": 14,
  "o": 15,
  "p": 16,
  "q": 17,
  "r": 18,
  "s": 19,
  "t": 20,
  "u": 21,
  "v": 22,
  "w": 23,
  "x": 24,
  "y": 25,
  "z": 26,
  ".": 27,
  "?": 28,
  "!": 29,
  ",": 30,
  "1": 31,
  "2": 32,
  "3": 33,
  "4": 34,
  "5": 35,
  "6": 36,
  "7": 37,
  "8": 38,
  "9": 39,
  "0": 40,
}

weight = [0,0,0,0,0,0]

bias = 0

def ask():
  ignore = ["what", "is", "a", "an", "are", "how", "why", "how", "when"]
  #Turn the query into a list 1
  print("Ken: Search Anything")
  #query = input("Search: ").lower()
  query = "physics"
  process = query.translate(str.maketrans('', '',string.punctuation))
  ask = process.split()

  priority = []
  for i in ask:
    if i not in ignore:
      priority.append(i)
    else:
      continue
  result = search(priority[0])

  phrase = parse(result)

  print(result)

def parse(result):
  #parse results with network() 3
  code = []
  for a in result:
    if a in letters: 
      bit = letters[a]
    else:
      bit = 0
    tuple = a, bit
    code.append(tuple)
  
  weighted_results = network(code)
    

def search(subheading):
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

  try:
     session = requests.Session()
     response = session.get(url, headers=headers, timeout=10)
     response.raise_for_status()

     soup = BeautifulSoup(response.text, 'html.parser')
     result1 = soup.find("div", class_="mw-parser-output")
     result = result.find('p')
     return result

  except Exception as e:
   print("Error: {e}")
   return "No Info Found"

def construct():
  #construct a response 4
  pass

def network(code):
  #evaluate encoded data 3a
  word_pass = []
  for b, c in code:
    if iter > 6 or iter < 0:
      iter = 0
    weight_i = weight[iter]
    value = neuron(c, weight_i)
    if value >= 0.8:
      word_pass.append(b)
    iter += 1

  return word_pass
  
def neuron(input, weight):
  #Calculate a Sigmoid for the value entered
  output = input * weight
  weight_result = 1 / ((math.e ** (output * -1)) + 1)
  weight_result += bias

  return weight_result

ask()
