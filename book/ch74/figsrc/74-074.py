import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(58)
cx, cy = 15, 32
pts = [(cx + (9 if k % 2 == 0 else 4)*math.cos(math.pi/2 + k*math.pi/5), cy + (9 if k % 2 == 0 else 4)*math.sin(math.pi/2 + k*math.pi/5)) for k in range(10)]
poly(ax, pts, 'autre')
for i in range(4): disc(ax, 35 + 6*i, 32, 1.8, 'autre')
arrow(ax, (35, 21), (53, 21), 'varie', both=True)
for i in range(3):
    for j in range(3): disc(ax, 67 + 6*i, 26 + 6*j, 1.8, 'sujet')
arrow(ax, (65, 18), (81, 18), 'varie', both=True); arrow(ax, (85, 24), (85, 40), 'varie', both=True)
for x, lab, r in [(15, 'figure finie', 'autre'), (44, 'frise', 'autre'), (73, 'papier peint', 'sujet')]:
    text(ax, x, 51, lab, r, 'm')
text(ax, 15, 12, 'aucune translation', 'autre', 's'); text(ax, 44, 12, '1 direction', 'autre', 's'); text(ax, 73, 12, '2 directions', 'sujet', 's')
save(fig, '74-074')
