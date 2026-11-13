import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, r'$x^2+1$ sur $\mathbb{R}$', 'sujet', 'm')
arrow(ax, (2, 24), (43, 24), 'fixe', lw=0.9)
text(ax, 38, 19.5, r'$x$', 'fixe', 's')
pts = [(22 + t * 12, 24 + 5 + (t ** 2) * 10) for t in [i / 10 for i in range(-15, 16)]]
line(ax, pts, 'sujet', lw=1.2)
text(ax, 22, 14, 'ne coupe pas l’axe', 'limite', 's')
box(ax, 50, 46, 36, 12, 'varie', label='facteur de degré 1', size='s')
arrow(ax, (68, 45.5), (68, 38.5), 'varie')
box(ax, 50, 26, 36, 12, 'limite', label='donnerait une racine', size='s', dash=True)
arrow(ax, (68, 25.5), (68, 18.5), 'limite')
box(ax, 50, 6, 36, 12, 'resultat', label='donc irréductible', size='s')
save(fig, '61-091')
