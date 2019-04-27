import core
import sys
import numpy as np

#train_data = open(sys.argv[1], 'r')
train_data = open('train_data', 'r')
melodies = []
num = -1
for line in train_data:
    if line[0] == '!':
        num += 1
        melodies += [[]]
    elif line[0] != '\n':
        melodies[num] += [list(map(float, line.split()))]

model = core.NN_model()
model.load()
train_in = []
train_out = []
for melody in melodies:
    print(melody)
    for i in range(0, len(melody) - 3):
        train_in += [[melody[i+1][0], melody[i+2][0], melody[i+3][0], melody[i][1], melody[i][2], i/len(melody)]]
        train_out += [melody[i][0] - 1]

print(train_in)
print(train_out)

model.train(np.array(train_in), np.array(train_out))
model.save()
