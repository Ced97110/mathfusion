import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# couples : (a,b)=(1,2) ~ (a',b')=(2,4) ; (c,d)=(1,3) ~ (c',d')=(2,6)
a, b, a2, b2, c, d, c2, d2 = 1, 2, 2, 4, 1, 3, 2, 6
assert (a * d + b * c) * b2 * d2 == 120 and (a2 * d2 + b2 * c2) * b * d == 120
assert a * b2 * d * d2 == 72 == b * a2 * d * d2 and c * d2 * b * b2 == 48 == d * c2 * b * b2
text(ax, 22, 94, 'départ : deux équivalences', 'fixe', 's')
box(ax, 2, 80, 40, 9, 'fixe', label=r'(1, 2) $\sim$ (2, 4)', size='m')
box(ax, 46, 80, 40, 9, 'fixe', label=r'(1, 3) $\sim$ (2, 6)', size='m')
box(ax, 2, 62, 84, 10, 'sujet', label=r'gauche : $5\times4\times6=120$', size='m')
cols = [(26, '72', 'fixe', r'$=$ car (1, 2) $\sim$ (2, 4)'), (62, '48', 'varie', r'$=$ car (1, 3) $\sim$ (2, 6)')]
for cx, v, role, why in cols:
    arrow(ax, (cx, 62), (cx, 56), 'varie')
    box(ax, cx - 10, 44, 20, 12, role, label=v, size='l')
    text(ax, cx, 37, why, 'resultat', 's')
    box(ax, cx - 10, 18, 20, 12, role, label=v, size='l')
    arrow(ax, (cx, 12), (cx, 18), 'varie')
box(ax, 2, 2, 84, 10, 'autre', label=r'droite : $20\times2\times3=120$', size='m')
save(fig, '54-053')
