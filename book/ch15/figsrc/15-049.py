import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$ab + ac = a(b + c)$', 'sujet', 'l')
text(ax, 44, 64.5, 'départ : la distributivité', 'fixe', 's')
s, g = 4.8, 0.8
x0 = (88 - (13 * s + 12 * g + 2)) / 2
p1 = [x0 + i * (s + g) + (2 if i >= 8 else 0) for i in range(13)]
for x in p1: box(ax, x, 46, s, s, 'varie', lw=0.6, r=0.4)
brace(ax, p1[0], p1[7] + s, 51.4, 'sujet', r'$8x$', down=False)
brace(ax, p1[8], p1[12] + s, 51.4, 'sujet', r'$5x$', down=False)
x1 = (88 - (13 * s + 12 * g)) / 2
p2 = [x1 + i * (s + g) for i in range(13)]
for x in p2: box(ax, x, 16, s, s, 'varie', lw=0.6, r=0.4)
brace(ax, p2[0], p2[12] + s, 15.4, 'resultat', r'$13x$')
arrow(ax, (44, 44.5), (44, 23.5), 'varie')
text(ax, 48, 34, r'$a = x,\ b = 8,\ c = 5$', 'varie', 's', ha='left')
text(ax, 44, 4, r'chaque carré $= x$', 'fixe', 's')
save(fig, '15-049')
