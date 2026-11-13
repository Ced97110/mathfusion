import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$\pi(x, y) = (y, 0)$ : sans $\pi\circ\pi=\pi$', 'limite', 's')
box(ax, 3, 42, 22, 10, 'sujet', label='(3, 5)')
box(ax, 33, 42, 22, 10, 'varie', label='(5, 0)')
box(ax, 63, 42, 22, 10, 'limite', label='(0, 0)')
arrow(ax, (26.5, 47), (31.5, 47), 'varie', lw=1.1)
arrow(ax, (56.5, 47), (61.5, 47), 'varie', lw=1.1)
text(ax, 29, 51, r'$\pi$', 'varie', 's')
text(ax, 59, 51, r'$\pi$', 'varie', 's')
text(ax, 44, 36, r'$\pi\circ\pi(3,5)=(0,0)$, non $(5,0)$', 'limite', 's')
# axe horizontal = image = noyau
line(ax, [(6, 18), (80, 18)], 'sujet', lw=2.2)
for x in (6, 80):
    ax.plot([x, x], [16.6, 19.4], color=COL['sujet'], lw=1.0)
text(ax, 44, 24, 'image = noyau = cet axe', 'sujet', 's')
text(ax, 44, 11, 'commun : tout l’axe', 'limite', 's')
text(ax, 44, 6, 'pas que 0 : non directe', 'limite', 's')
save(fig, '58-281')
