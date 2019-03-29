import random as rnd

rhytms_half = [[[0, 0.5, 1, 0]], [[0, 0.25, 1, 0], [0, 0.25, 0, 0]], [[0, 1/4, 1, 0], [0, 1/8, 0, 0], [0, 1/8, 0, 0]], [[0, 1/8, 1, 0], [0, 1/8, 0, 0], [0, 1/4, 0, 0]]]
rhytms_fourth = [1/4, []]

a = []
for i in range(0, 8):
    a += rhytms_half[rnd.randint(0,3)]
print(a)