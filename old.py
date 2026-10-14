import json
import re
import string
import math

trains = [
  ([1, 0, 0, 1, 0, 0], 0),
  ([1, 1, 1, 1, 1, 0], 0),
  ([0, 0, 0, 1, 0, 0], 0),
  ([0, 1, 0, 0, 0, 1], 0),
  ([0, 1, 1, 1, 1, 0], 0),
  ([0, 1, 1, 0, 1, 1], 0),
  ([1, 0, 1, 0, 1, 0], 0),
  ([0, 0, 0, 0, 0, 0], 0),
  ([0, 1, 0, 1, 0, 1], 0),
  ([1, 0, 0, 0, 1, 0], 0),
  ([1, 0, 1, 0, 1, 1], 0),
  ([0, 0, 0, 0, 1, 0], 0),
  ([1, 0, 1, 0, 0, 0], 0),
  ([1, 0, 0, 0, 1, 0], 0),
]

ignore = ["if", "what", "of", "a", "an", "and", "is"]

act = 0
count = 0

weights2 = []

bias2 = []

def fileread(file):
  with open(file, "r") as file:
            file_content = file.read()
            content = json.loads(file_content)
  return content

def create(word):
  global weights2, bias2
  rate = 1
  prevkey = [[1,0,0,1,0,1], [1,1,1,1,0,1], [0,1,1,1,1,0]]
  for i in range(3):
   if i == 1:
     prevkey = [[0,1,0,1,1,1], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1]]
   if i == 2:
     prevkey = [[1,1,1,1,1,0], [1,1,1,1,1,1]]
   trainpre = prevkey
    
   prew = [-1.5194, 1.9066, -0.0845, 0.1442, 0.9803, -1.2551]
   preb = 0

   copy = trains.copy()
  
   for key in trainpre:
     key2 = []
     for c in range(len(key)):
        word[c] += key[c]
     for e in word:
        key2.append(0 if e % 2 == 0 else 1)

     key3 = key2, 1
     copy.append(key3)

   for q in range(20):
    for exe in range(250):
     for val, exp in copy:
      result = trainneuron(val, prew, preb, i)
      reced = exp - result
      grad = reced * result * (1 - result)
      for e in range(len(prew)):
        we2 = None
        we2 = prew
        we2[e] += rate * grad * val[e]
      preb += rate * grad
     
   weights2.append(prew)
   bias2.append(preb)

   del copy
   word = trainpre[0]
  print(weights2, bias2)
  return

def trainneuron(input, prew, preb, z):
    global act, count
      
    output = 0
    output3 = 0
    for i in range(6):
      output += input[i] * prew[i]

    output += preb
    output3 = 1 / ((2.718 ** (output * -1)) + 1)

    return output3

def generate(prev_word, answer, worddef, isa):
  act = 0
  response = []
  toggle = True

  response.append(prev_word)
  
  vocabulary = fileread('vocab.json')
  code = vocabulary[prev_word]
  create(code)

  while toggle:
    prev_val = vocabulary[prev_word]
    word = finder(prev_val)
    if len(response) > 10:
      word = worddef
      toggle = False
    if word == "end":
      toggle = False
    if word == "output":
      if worddef is not None and isa is not None:
        word = f"{worddef} and {isa}"
      elif worddef is not None:
        word = worddef
      elif isa is not None:
        word = isa
      else:
        if isinstance(word, list):
          word = " ".join(word)
        else:
          word = word.strip("[]''")
      toggle = False
    response.append(word)
    prev_word = word
    
  response_final = " ".join(response)
  print(f"{response_final}")
  return

def neuron2(input):
    global act, count
      
    output = 0
    output3 = 0
    for i in range(6):
      we = None
      we = weights2[act]
      output += input[i] * we[i]

    output += bias2[act]
    output3 = 1 / ((2.718 ** (output * -1)) + 1)

    return output3
    
def finder(value):
  global act
  predictions = {}
  outputs = []
  decimals = []
  vocablist = None
  
  for a in vocab:
    vocablist = vocab[a].copy()
    
    for c in range(len(value)):
      vocablist[c] += value[c]

    betterinputs = []
    for d in vocablist:
      betterinputs.append(0 if d % 2 == 0 else 1)

    result = neuron2(betterinputs)
    #if a == "is" or a == "a":
      #print(a, betterinputs, result)
    predictions[f"{a}"] = f"{result}"
    outputs.append(a)
    decimals.append(result)

  softmax = lambda x: [math.exp(i - max(x)) / sum(math.exp(j - max(x)) for j in x) for i in x] #just staight up stole this :)
  finals = softmax(decimals)
  
  for b in range(len(finals)):
    predictions[f"{outputs[b]}"] = f"{finals[b]}"
    #predictions[f"{outputs[b]}"] = f"{decimals[b]}"

  greatest = 0
  next_word = None
  for c in predictions:
    candid = 0
    candid = predictions[c]
    candid = float(candid)
    if candid > greatest:
      greatest = candid
      next_word = c
  
  #woah = predictions[next_word]
  #print(f"{next_word}: {woah}")

  if act == 1:
      act = 2
  elif act == 2:
      act = 0
  else:
      act = 1

  return next_word
  
def analyze(file_path, target_phrase1, victor):
    file_content = ""
    fact = None
    fact2 = None
    current_item2 = "APLACEHOLDEr"
    attributeslist = []
    attributeslist2 = []
    target_phrase = []
    worddef = None
    isa = None
  
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            json_data = json.loads(file_content)
            current_item = json_data
        win = victor - 1
        for item in target_phrase1:
         if target_phrase1[win] != 0:
           target_phrase2 = target_phrase1[win]
           target_phrase.append(target_phrase2)
           break
         else:
           win += 1
           continue
        for w in target_phrase1:
	        target_phrase.append(w)
        if target_phrase2 == "0":
          for object in target_phrase:
            if object != "0":
              target_phrase2 = object

        for a in target_phrase:
             if a in ignore:
                continue
             if a in current_item2:
                fact2 = current_item2[a]
                specs = fact2
                attributeslist.append(fact2)
                attributeslist2.append(fact2)
                continue
             if a in current_item:
                fact = current_item[a]
                attributeslist.append(fact)
                current_item2 = fact
                current_item = fact
                fact4 = None
                if 'definition' in current_item:
                    worddef = current_item['definition']
                if '_is_a' in current_item:
                    fact4pre = current_item['_is_a']
                    fact4 = json_data[fact4pre]
                    isa = fact4['definition']
                    attributeslist.append(fact4)
                if '_sentence' in current_item:
                  setup = current_item['_sentence']

        if attributeslist:
          if fact2 is not None:
            attributeslist = f"{attributeslist2}"
         
          return attributeslist, worddef, isa, target_phrase2

        else:
          print("No response found.")
          return None
          
    except Exception as e:
        print(f"An error occurred during json or a answer might not be known: {e}")
        return None

def parse(terms):
  main = None
  codedex = None
  property1 = False
  newterm = None

  try:
    item = fileread('config.json')

    for h in terms:
      if h in item:
        main = h
        break

    if main is not None:
      newterm = [main]
      for term_item in terms:
        if term_item != main:
          newterm.append(term_item)
        if 'code' in item[main] and isinstance(item[main]['code'], list):
            codedex = item[main]['code']
      for _ in range(2):
        newterm.append("0")

    else:
      print("No input detected or main term not found in JSON data.")
      return

    return newterm, codedex
    
  except Exception as e:
    print(f"An error occured during parsing: {e}")
    return

def values(value):
  inputs = [0, 0, 0, 0, 0, 0]

  for c in range(len(value)):
    inputs[c] += value[c]

  betterinputs = []

  for d in inputs:
      betterinputs.append(0 if d % 2 == 0 else 1)

  list1 = betterinputs

  return list1

def neuron(inputt, setcheck, act):
    output = 0
    output3 = 0
    austria = []
    poland = []

    for i in range(3):
      we = None
      we = weights[act]
      output += inputt[i] * we[i]
      
    if len(setcheck) < 3:
      for i in range(3):
        we = None
        we = weights[act]
        output += inputt[i + 3] * we[i]

    output += bias[act]
    output3 = 1 / ((2.718 ** (output * -1)) + 1)

    return output3

def think(o):
  global act

  poland = []
  austria = []
  
  for _ in range(3):
    hello1 = values(o)
    hello2 = neuron(hello1, poland, act)
    if hello2 is not None:
      poland.append(hello2)
    act += 1
    
  for _ in range(3):
      hello3 = neuron(poland, poland, act)
      if hello3 is not None:
        austria.append(hello3)
      act += 1

  for _ in range(1): #New layers
    for _ in range(3):
      hello3 = neuron(austria, poland, act)
      del austria[0]
      if hello3 is not None:
        austria.append(hello3)
      act += 1

  final = 0
  ins = 0
  for f in austria:
    ins += 1
    if f > final:
      final = f
      winner = ins
      finish = f"Number {ins}: {f}"
  act = 0
 
  return winner
  
def command(processed):
  
    newterm, codedex = parse(processed)
    print("Request Parsed!")
  
    victor = think(codedex)
    print("Priorities Found!")

    results, worddef, isa, target_phrase2 = analyze("config.json", newterm, victor)
    print("Data Retrieved!")
    
    finish = generate(target_phrase2, results, worddef, isa)
  
def start():
  print("------Ken v.2------")
  #inquiry = inpt("Question: ").lower()
  inquiry = "python"
  process1 = inquiry.translate(str.maketrans('', '',string.punctuation))
  processed = process1.split()

  command(processed)
  
start()
