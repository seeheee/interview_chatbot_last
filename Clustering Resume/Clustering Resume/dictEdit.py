import os

f = open('dict.txt', 'rt', encoding='utf-8')
info = []
while True:
    line = f.readline()
    if not line: break
    info.append(line)

text = "".join(info).replace(" ", " ").replace('"', '').replace("'", "").replace("+", "").split("), (")
topic = text
for i in range(len(topic)):
    topic[i] = topic[i].split('  ')
    topic[i][0] = topic[i][0][3:].strip()
weight = []
word = []
# for i in range(len(topic)):
n = 4
for i in range(len(topic[n])):
    topic[n][i] = topic[n][i].split('*')
    weight.append(topic[n][i][0])
    word.append(topic[n][i][1])

print(weight)
print(word)

end = {}
for i in range(len(weight)):
    end[word[i]] = weight[i]

print(end)
