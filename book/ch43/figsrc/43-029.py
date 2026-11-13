import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 12, 74, 64, 10, 'fixe', label='15 − 3 est un multiple de 12', size='s')
arrow(ax, (44, 73), (44, 62), 'varie'); text(ax, 48, 67.5, 'même sens, plus court', 'varie', 's', ha='left')
box(ax, 12, 51, 64, 10, 'sujet', label='15 est congru à 3 modulo 12', size='s')
cx, cy, R = 30, 27, 16
for n in range(12):
    x, y = cx + R*math.sin(math.radians(30*n)), cy + R*math.cos(math.radians(30*n))
    disc(ax, x, y, 1.6, 'sujet' if n == 3 else 'fixe')
text(ax, cx, cy, 'même place', 'fixe', 's')
px = cx + R
for lab, y in (('15', 33), ('3', 21)):
    arrow(ax, (px+2, cy), (60, y), 'fixe', lw=0.6); text(ax, 63, y, lab, 'sujet', 'm', ha='left')
save(fig, '43-029')
