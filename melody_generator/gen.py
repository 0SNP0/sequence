import sys
import core
import numpy as np
import random

qpm = sys.argv[1]
tonality = sys.argv[2]
takts = int(sys.argv[3])

rhytms_half = [[[0, 0.5, 1, 0]], [[0, 0.25, 1, 0], [0, 0.25, 0, 0]], [[0, 1/4, 1, 0], [0, 1/8, 0, 0], [0, 1/8, 0, 0]], [[0, 1/8, 1, 0], [0, 1/8, 0, 0], [0, 1/4, 0, 0]]]
a = []
for i in range(0, takts*2):
    a += rhytms_half[random.randint(0,len(rhytms_half)-1)]
print(a)

melody = [[random.randint(1,7), a[-3][1]], [random.randint(1,7), a[-2][1]], [random.randint(1,7), a[-1][1]]]

model = core.NN_model()
model.load()

for i in range(len(a)-4, -1, -1):
    melody = [[model.apredict(a[i+1][0], a[i+2][0], a[i+3][0], a[i][1], a[i][2], i/len(a)), a[i][1]]] + melody
print(melody)

file = open('melody.seq', 'w')
file.write(qpm + ' ' + tonality + '\n')
for note in melody:
    for p in note:
        file.write(str(p) + ' ')


