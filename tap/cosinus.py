import math
F1 = 'primul laborator primul exercitiu'
F2 = 'primul exercitiu usor'
F1 = F1.replace(',','')
F1 = F1.replace('.','')
F2 = F2.replace(',','')
F2 = F2.replace('.','')

frequency1 = {}
frequency2 = {}

for word in F1.split(' '):
    if word not in frequency1.keys():
        frequency1[word] = 1
    else:
        frequency1[word] += 1

for word in F2.split(' '):
    if word not in frequency2:
        frequency2[word] = 1
    else:
        frequency2[word] += 1

words = []
for word in list(frequency1.keys()):
    words.append(word)
for word in list(frequency2.keys()):
    if word not in words:
        words.append(word)

up = 0
for word in words:
    if word not in frequency1.keys():
        frequency1[word] = 0
    if word not in frequency2.keys():
        frequency2[word] = 0
    up += frequency2[word] * frequency1[word]

down1 = 0
down2 = 0
for word in words:
    down1 += frequency1[word] * frequency1[word]
for word in words:
    down2 += frequency2[word] * frequency2[word]
down = math.sqrt(down1) * math.sqrt(down2)
print(up/down)