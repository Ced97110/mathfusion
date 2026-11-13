import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
k = 2.0; y0 = 20
for x, xv, v, role, note in [(18, r'$x=-2$', 21, 'limite', 'faux'), (44, r'$x=-1$', 13, 'resultat', 'vrai'), (70, r'$x=0$', 5, 'resultat', 'vrai')]:
    box(ax, x - 8, y0, 16, v * k, role, r=0.4)
    text(ax, x, y0 + v * k + 4, str(v), role, 'm')
    text(ax, x, y0 - 4, xv, 'encre', 's'); text(ax, x, y0 + 5, note, role, 's')
line(ax, [(4, y0 + 14 * k), (84, y0 + 14 * k)], 'sujet', lw=1.0, dash=True)
text(ax, 86, y0 + 14 * k + 3, '14', 'sujet', 's', ha='right')
arrow(ax, (14, 77), (70, 52), 'varie', lw=1.4)
text(ax, 62, 67, 'la valeur baisse', 'varie', 's')
arrow(ax, (8, 10), (62, 10), 'varie', lw=1.2)
text(ax, 64, 10, 'x augmente', 'varie', 's', ha='left')
line(ax, [(31, y0), (31, 84)], 'resultat', lw=1.0, dash=True)
arrow(ax, (31, 84), (84, 84), 'resultat', lw=1.4)
text(ax, 58, 88.5, 'solutions : à droite', 'resultat', 's')
text(ax, 44, 3, r'valeur de $-8x+5$', 'fixe', 's')
save(fig, '17-093')
