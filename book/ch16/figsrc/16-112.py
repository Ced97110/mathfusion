import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 14, 50, 60, 8, 'limite', dash=True, label=r'$x = 3$, mais $x$ = quoi ?', size='s')
u = 6
x0, y0 = 34, 24
poly(ax, [(x0, y0), (x0 + 7 * u, y0), (x0 + 7 * u, y0 + 3 * u), (x0, y0 + 3 * u)], 'fixe')
line(ax, [(x0, y0), (x0, y0 + 3 * u)], 'sujet', lw=2.4)
text(ax, x0 - 4, y0 + 9, 'largeur : 3', 'sujet', 's', rot=90)
text(ax, x0 + 3.5 * u, y0 + 9, 'longueur ?', 'fixe', 's')
box(ax, 3, 6, 40, 8, 'limite', label='réponse « 3 m » : faux', size='s')
box(ax, 46, 6, 39, 8, 'resultat', label='longueur : 7 m', size='s')
text(ax, 44, 17, 'question : la longueur', 'fixe', 's')
save(fig, '16-112')
