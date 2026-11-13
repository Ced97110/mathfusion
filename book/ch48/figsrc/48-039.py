import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ys = [52, 42, 32]
for y, n in zip(ys, ['1', '5', '9']):
    disc(ax, 14, y, 4.5, 'sujet', label=n, size='m')
    arrow(ax, (19, y), (59, 42 + (y - 42) * 0.4), 'fixe', lw=0.8)
disc(ax, 68, 42, 6, 'sujet', label='1', size='m')
text(ax, 38, 57, r'$f$', 'fixe', 'm')
text(ax, 68, 31, 'position 1', 'sujet', 's')
# back: red single, green set
arrow(ax, (62, 22), (36, 22), 'limite', lw=1.1)
text(ax, 49, 27, '✗', 'limite', 'l')
text(ax, 22, 22, 'un seul entier', 'limite', 's')
arrow(ax, (62, 9), (36, 9), 'resultat', lw=1.1)
text(ax, 22, 9, r'{1, 5, 9}', 'resultat', 'm')
text(ax, 49, 13.5, 'l’ensemble', 'resultat', 's')
save(fig, '48-039')
