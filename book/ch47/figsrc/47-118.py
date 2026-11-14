import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, 'Une donnée plus courte suffit-elle ?', 'encre', 'm')
f = lambda v: 44 + v * 3.8
for (y, m, role, lab) in [(44, 3, 'sujet', 'congruence modulo 3'), (22, 5, 'autre', 'congruence modulo 5')]:
    line(ax, [(4, y), (84, y)], role, lw=0.6)
    for v in range(-10, 11):
        if v % m == 0: disc(ax, f(v), y, 1.9, 'resultat')
        else: disc(ax, f(v), y, 0.6, 'fixe')
    disc(ax, f(0), y, 3.2, 'resultat', fill=False, lw=1.0)
    text(ax, 4, y + 7, lab, role, 's', ha='left')
    text(ax, f(0), y - 6, 'classe de 0', 'resultat', 's')
text(ax, 44, 6, r'$a\equiv b$ si $a-b$ est en vert', 'resultat', 's')
save(fig, '47-118')
