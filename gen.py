import sys
import os
import core
import numpy as np
import random

qpm = sys.argv[1]
tonality = sys.argv[2]
takts = int(sys.argv[3])
if len(sys.argv) > 4:
    midifile_name = sys.argv[4]
else:
    midifile_name = 'melody.mid'

rhytms_half = [[[0, 0.5, 1, 0]], [[0, 0.25, 1, 0], [0, 0.25, 0, 0]], [[0, 1/4, 1, 0], [0, 1/8, 0, 0], 
                [0, 1/8, 0, 0]], [[0, 1/8, 1, 0], [0, 1/8, 0, 0], [0, 1/4, 0, 0]]]
a = []
for i in range(0, takts*2):
    a += rhytms_half[random.randint(0,len(rhytms_half)-1)]
print(a)

melody = [[random.randint(1,7), a[-3][1]], [random.randint(1,7), a[-2][1]], [1, a[-1][1]]]

model = core.NN_model()
model.load()

for i in range(len(a)-4, -1, -1):
    melody = [[model.apredict(melody[0][0], melody[1][0], melody[2][0], a[i][1], a[i][2], i/len(a)), a[i][1]]] + melody
print(melody)
oct = 0
for i in range(1, len(melody)):
    if melody[i][0] == 1 and melody[i-1][0] == 1:
        chance = random.randint(1, 6)
        if chance == 1: melody[i][0] += 7
        elif chance == 2: melody[i-1][0] += 7
    else:
        if ((melody[i-1][0]-1) % 7) - ((melody[i][0]-1) % 7) > 5:
            oct += 1
        if ((melody[i][0]-1) % 7) - ((melody[i-1][0]-1) % 7) > 5:
            oct -= 1
    melody[i][0] += (7 * oct)
print(melody)

file = open('melody.seq', 'w')
file.write(qpm + ' ' + tonality + '\n')
for note in melody:
    for p in note:
        file.write(str(p) + ' ')
file.__exit__()

if sys.platform == "linux" or sys.platform == "linux2":
    os.system('./convert ' + midifile_name)
elif sys.platform == "win32":
    os.system('.\\convert.exe ' + midifile_name)
