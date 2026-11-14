import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 20, 83, 'mots de FM', 'sujet', 'm'); text(ax, 66, 83, r'$M$ : engendré par 2 et 3', 'resultat', 'm')
rows = [('mot vide', '1'), (r'$x$', '2'), (r'$y$', '3'), (r'$xx$', '4'), (r'$xy$', '6')]
for i, (w, v) in enumerate(rows):
    y = 66 - i * 11
    box(ax, 6, y - 4, 28, 9, 'sujet', label=w, size='s')
    box(ax, 58, y - 4, 16, 9, 'resultat', label=v, size='s')
    arrow(ax, (34.5, y + 0.5), (57.5, y + 0.5), 'varie', lw=1.3)
for cx in (20, 66):
    for k in range(3): disc(ax, cx, 14 - 3.4 * k, 0.5, 'fixe')
text(ax, 46, 75, r'$\eta$ : $x\mapsto 2$, $y\mapsto 3$', 'varie', 's')
text(ax, 44, 3, r'chaque élément de $M$ reçoit un mot', 'resultat', 's')
save(fig, '49-038')
