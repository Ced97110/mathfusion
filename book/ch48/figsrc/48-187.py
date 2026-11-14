import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(105)
text(ax, 44, 99, 'entiers n', 'sujet', 's')
X = lambda v: 8 + v * 6
line(ax, [(5, 90), (82, 90)], 'fixe')
for v in range(13):
    k = v % 4 == 0
    disc(ax, X(v), 90, 2.0 if k else 1.2, 'varie' if k else 'fixe')
    if k: text(ax, X(v), 83.5, str(v), 'varie', 's')
text(ax, 44, 76, 'noyau : 0, 4, 8, 12…', 'varie', 's')
arrow(ax, (44, 72), (44, 62), 'sujet'); text(ax, 48, 67, 'n ↦ n × 3', 'sujet', 's', ha='left')
c, r = (44, 36), 17
for k in range(12):
    a = math.pi / 2 - 2 * math.pi * k / 12; x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
    on = k % 3 == 0
    disc(ax, x, y, 2.6 if on else 1.4, 'resultat' if on else 'fixe', label=str(k) if on else None, size='s')
text(ax, 44, 36, 'image', 'resultat', 's'); text(ax, 44, 31, '4 éléments', 'resultat', 's')
text(ax, 44, 8, 'horloge à 12', 'fixe', 's')
save(fig, '48-187')
