import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 58, 66, 'côtés droits du signe égal', 'fixe', 's')
for y, r, t, g, d, nom in [(46, 'sujet', r'$B$', r'$x+y$', '5', 'ticket de lundi'), (22, 'autre', r'$D$', r'$2x+y$', '8', 'ticket de mardi')]:
    text(ax, 18, y + 5, nom, 'fixe', 's')
    box(ax, 33, y, 22, 10, 'fixe', fill=True, label=g)
    text(ax, 60, y + 5, '=', 'fixe', 'l')
    box(ax, 65, y, 14, 10, r, fill=True, label=d)
    arrow(ax, (72, y), (72, y - 4), r, lw=0.9)
    disc(ax, 72, y - 7.2, 3.2, r, label=t, size='m')
box(ax, 18, 1, 62, 8, 'resultat', fill=True, label=r'$B+D=5+8=13$')
save(fig, '24-050')
