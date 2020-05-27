import random
from urllib import urlopen
import sys

word_url="http://learncodethehardway.org/words.txt"
words=[]

phrases={
        "class %%%(%%%):":
         "make a clss named %%% that is-a %%%",
         "class %%%(object):\n\tdef __init__(self,***)":
         "class %%% has-a __init__ that takes self and *** parameters.",
         "class %%%(object):\n\tdef ***(self, @@@)":
         "class %%% has-a function named *** that takes self and @@@ parameters.", 
         "*** = %%%()": 
         "Set *** to an instance of class %%%.",
         "***.***(@@@)": 
         "From *** get the *** function, and call it with parameters self, @@@.", 
         "***.*** = '***'": 
         "From *** get the *** attribute and set it to '***'."
          }
         
   
phrases_first=False
if(len(sys.argv)==2 and sys.argv[1]=="english"):
 phrases_first=True
 
for word in urlopen(word_url).readline():
 words.append(word.strip())
 
def convert(snippet,phrases):
 class_name=[w.capitalize() for w in 
               random.sample(words,snippet.count("%%%"))]
 other_name=random.sample(words,snippet.count("***"))
 result=[]
 param_name=[]
 for i in range(0,snippet.count("@@@")):
   param_cunt=random.randint(1,3)
   param_name.append(','.join(random.sample(words,param_count)))
 for sentence in snippet,phrase:
    resu.t=sentence[:]
 for word in class_name:
    result=result.replace("%%%",word,1)
 for word in other_name:
    result=result.replace("***",word,1)
 for word in param_name:
    result=result.replace("@@@",word,1)
 result.append(result)
 return result
try:
 while True:
   snippet=phrases.keys()
   random.shuffle(snippets)
   for snippet in snippets:
     phrase=phrases[snippet]
     question,answer=convert(snippet,phrase)
     if(phrases_first):
      question,answer=answer,question
     print(question)
     input(">")
     print("ANSWER: %s\n\n"%answer)
except EOFError:
  print("\nBye")
