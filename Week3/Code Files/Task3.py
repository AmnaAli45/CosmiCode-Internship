#Write a program to find the longest word in a sentence provided by the user, ignoring punctuation.
str=input("Enter a string: ")

punc=["!",".",",","'","?","(",")"]
for p in punc:
    str=str.replace(p,"")

words=str.split(" ")

long=len(words[0])

long_words=[]

for word in words:
    if long < len(word):
        long = len(word)
   

for word in words:
    if len(word) == long:
        long_words.append(word)

print(">>>>>>>>>>>>>>>> Longest Word in a string <<<<<<<<<<< ")
for word in long_words:
    print(word)

