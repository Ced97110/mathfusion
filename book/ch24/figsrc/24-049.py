import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 38, 58, 'côtés gauches du signe égal', 'fixe', 's')
for y, r, t, g, d, nom in [(36, 'sujet', r'$A$', r'$x+y$', '5', 'ticket de lundi'), (8, 'autre', r'$C$', r'$2x+y$', '8', 'ticket de mardi')]:
    text(ax, 40, y + 14, nom, 'fixe', 's')
    disc(ax, 8, y + 5, 4.2, r, label=t, size='l')
    arrow(ax, (12.6, y + 5), (19, y + 5), r, lw=0.9)
    box(ax, 20, y, 34, 10, r, fill=True, label=g)
    brace(ax, 20, 54, y - 0.5, r, label='côté gauche')
    text(ax, 60, y + 5, '=', 'fixe', 'l')
    text(ax, 72, y + 5, d, 'fixe', 'm')
save(fig, '24-049')
