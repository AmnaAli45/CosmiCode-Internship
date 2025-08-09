#Write a program to find the most frequent word in a text file.
with open("text.txt", "r") as f:
    data = f.read()


punc=["!",".",",","'","?","(",")","\n"]
for p in punc:
    data=data.replace(p,"")
data = data.lower()
words = data.split(" ")


freq=[]
for i in range (len(words)):
    frequency = 0
    for word in words:
        if word == words[i]:
            frequency += 1
    freq.append(frequency)

match = []
max_frequency = max(freq)
for i in range (len(freq)):
    if max_frequency == freq[i] and words[i] not in match:
        match.append(words[i])

for word in match:
    print(word)
        




