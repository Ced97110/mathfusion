import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
# four panels 2 x 2
panels = [(2, 36), (46, 36), (2, 4), (46, 4)]
for (x, y) in panels:
    box(ax, x, y, 40, 28, 'fixe', fill=False)
text(ax, 8, 60, r'$\mathbb{Z}$', 'sujet', 'l')
text(ax, 22, 48, '5 + 9 = 14', 'resultat', 'm')
text(ax, 52, 60, r'$\mathbb{Z}^2$', 'sujet', 'l')
text(ax, 66, 48, '(2 ; 1)+(6 ; 3)', 'resultat', 's')
text(ax, 66, 42.5, '= (8 ; 4)', 'resultat', 's')
text(ax, 10, 28, r'$\mathbb{R}^2$', 'sujet', 'l')
text(ax, 22, 16, '(1,5 ; 2)+(0,5 ; 1)', 'resultat', 's')
text(ax, 22, 10.5, '= (2 ; 3)', 'resultat', 's')
# clock Z/12Z
cx, cy, r = 56, 20, 9
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(12):
    a = math.radians(90 - 30 * k)
    role = 'varie' if k == 9 else ('resultat' if k == 2 else 'fixe')
    rr = 1.1 if role != 'fixe' else 0.6
    disc(ax, cx + (r) * math.cos(a), cy + r * math.sin(a), rr, role)
text(ax, 84, 28, r'$\mathbb{Z}/12\mathbb{Z}$', 'sujet', 's', ha='right')
text(ax, 74, 10, '9 h + 5 h = 2 h', 'resultat', 's')
save(fig, '57-035')
