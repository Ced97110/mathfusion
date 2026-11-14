import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
oy = 28
for cx, title, eqs in [(22, 'système 1', r'$x+y=0$ et $2x+2y=0$'), (66, 'système 2', r'$x+y=0$ et $x-y=0$')]:
    text(ax, cx, 66, title, 'sujet', 'm', weight='bold')
    text(ax, cx, 60, eqs, 'fixe', 's')
    arrow(ax, (cx - 17, oy), (cx + 17, oy), 'fixe', lw=0.7)
    arrow(ax, (cx, oy - 16), (cx, oy + 17), 'fixe', lw=0.7)
    text(ax, cx + 18.5, oy, r'$x$', 'fixe', 's')
    text(ax, cx + 2.5, oy + 19, r'$y$', 'fixe', 's')
# système 1 : une seule droite, toute la droite est solution
line(ax, [(22 - 14, oy + 14), (22 + 14, oy - 14)], 'resultat', lw=1.4)
disc(ax, 22 + 7, oy - 7, 1.6, 'resultat')
text(ax, 22 + 10, oy - 7, r'$(1,\ -1)$', 'resultat', 's', ha='left')
disc(ax, 22, oy, 1.4, 'fixe')
text(ax, 22 - 3, oy - 4, r'$(0,\ 0)$', 'fixe', 's', ha='right')
# système 2 : deux droites, seul le point (0, 0)
line(ax, [(66 - 14, oy + 14), (66 + 14, oy - 14)], 'fixe', lw=1.2)
line(ax, [(66 - 14, oy - 14), (66 + 14, oy + 14)], 'fixe', lw=1.2)
disc(ax, 66, oy, 1.4, 'fixe')
text(ax, 66, oy - 5, r'$(0,\ 0)$', 'fixe', 's')
save(fig, '70-032')
