import math
import json
from bs4 import BeautifulSoup
import requests
import string

letters = {
  " ": 41,
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

vocab = {
  "python": [1,1,0,1,1,0],
  "javascript": [1,1,0,1,1,0],
  "kenadian": [1,1,1,0,0,0],
  "programming language": [1,1,1,0,0,1],
  "youtuber": [1,1,1,0,0,1],
  "founder": [1,1,1,0,1,0],
  "is": [1,0,0,1,0,1],
  "end": [1,1,1,1,1,1],
  "output": [1,1,1,1,1,0],
  "year": [1,1,1,1,0,0],
  "what": [0, 0, 0, 0, 0, 1],
  "how": [0, 0, 0, 0, 1, 0],
  "why": [0, 0, 0, 0, 1, 1],
  "who": [0, 0, 0, 1, 0, 0],
  "where": [0, 0, 0, 1, 0, 1],
  "when": [0, 0, 0, 1, 1, 0],
  "which": [0, 0, 0, 1, 1, 1],
  "whose": [0, 0, 1, 0, 0, 0],
  "whom": [0, 0, 1, 0, 0, 1],
  "whether": [0, 0, 1, 0, 1, 0],
  "and": [0, 0, 1, 0, 1, 1],
  "but": [0, 0, 1, 1, 0, 0],
  "or": [0, 0, 1, 1, 0, 1],
  "so": [0, 0, 1, 1, 1, 0],
  "because": [0, 0, 1, 1, 1, 1],
  "although": [0, 1, 0, 0, 0, 0],
  "unless": [0, 1, 0, 0, 0, 1],
  "while": [0, 1, 0, 0, 1, 0],
  "since": [0, 1, 0, 0, 1, 1],
  "though": [0, 1, 0, 1, 0, 0],
  "of": [0, 1, 0, 1, 0, 1],
  "to": [0, 1, 0, 1, 1, 0],
  "in": [0, 1, 0, 1, 1, 1],
  "for": [0, 1, 1, 0, 0, 0],
  "on": [0, 1, 1, 0, 0, 1],
  "with": [0, 1, 1, 0, 1, 0],
  "at": [0, 1, 1, 0, 1, 1],
  "by": [0, 1, 1, 1, 0, 0],
  "from": [0, 1, 1, 1, 0, 1],
  "about": [0, 1, 1, 1, 1, 0],
  "through": [0, 1, 1, 1, 1, 1],
  "between": [1, 0, 0, 0, 0, 0],
  "under": [1, 0, 0, 0, 0, 1],
  "against": [1, 0, 0, 0, 1, 0],
  "the": [1, 0, 0, 0, 1, 1],
  "a": [1, 0, 0, 1, 0, 0],
  "an": [1, 0, 0, 1, 0, 1],
  "this": [1, 0, 1, 1, 0, 0],  
  "these": [1, 0, 1, 0, 0, 0],
  "those": [1, 0, 1, 0, 0, 1],
  "it": [1, 0, 1, 0, 1, 0],
  "its": [1, 0, 1, 0, 1, 1],
  "they": [1, 0, 1, 1, 0, 0],
  "them": [1, 0, 1, 1, 0, 1],
  "their": [1, 0, 1, 1, 1, 0],
  "am": [1, 1, 0, 0, 0, 0],
  "are": [1, 1, 0, 0, 0, 1],
  "was": [1, 1, 0, 0, 1, 0],
  "were": [1, 1, 0, 0, 1, 1],
  "means": [1,1,1,1,0,1]
}

weight = [0,0,0,0,0,0]
bias = 0

weights2 = [0,0,0,0,0,0]
bias2 = 0

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

  request = priority[0]
  
  result = search(priority[0])
  if result == None:
    print("No Results")
  else:
    phrase = parse(result)

    construct(phrase, request)

def parse(result):
  #parse results with network() 3
  code = []
  bits = result.translate(str.maketrans('', '',string.punctuation))
  word_list = bits.split()
  for b in word_list:
   bit = 0
   for a in b:
    if a in letters: 
      bit += letters[a]
    else:
      pass
   tuple = b, bit
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
     result = result1.find('p')
     return result

  except Exception as e:
   print(f"Error: {e}")
   return "No Info Found"

def construct(phrase, request):
  #construct a response 4
  #answer = " ".join(phrase)
  print(phrase)

def network(code):
  #evaluate encoded data 3a
  word_pass = []
  iter = 0
  for c, d in code:
    if iter > 5 or iter < 0:
      iter = 0
    weight_i = weight[iter]
    value = neuron(c, weight_i)
    if value >= 0.8:
      word_pass.append(b)
    iter += 1

  return word_pass
  
def neuron(input, weightA):
  #Calculate a Sigmoid for the value entered
  output = input * weightA
  weight_result = 1 / ((math.e ** (output * -1)) + 1)
  weight_result += bias

  return weight_result

ask()
