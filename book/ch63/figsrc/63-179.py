import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# aller : corps -> groupe -> corps fixe
text(ax, 44, 72, 'départ, puis retour par Gal puis Inv', 'fixe', 's')
box(ax, 2, 50, 20, 12, 'sujet', label=r'$\mathbb{Q}$')
box(ax, 34, 50, 20, 12, 'fixe', label=r'$\{1\}$')
box(ax, 64, 50, 22, 12, 'limite', label=r'$\mathbb{Q}(r)$')
arrow(ax, (23, 56), (33, 56), 'varie')
arrow(ax, (55, 56), (63, 56), 'varie')
text(ax, 28, 61.5, 'Gal', 'varie', 's')
text(ax, 59, 61.5, 'Inv', 'varie', 's')
# on attendait de retrouver Q : arc en pointillé rouge
arrow(ax, (75, 49), (12, 49), 'limite', curve=-0.5)
text(ax, 44, 43, r'$\neq$', 'limite', 'xl')
# emboîtement : Q dans Q(r), strict
box(ax, 8, 6, 72, 20, 'limite', label=None, dash=True)
box(ax, 14, 11, 22, 10, 'sujet', label=r'$\mathbb{Q}$')
text(ax, 58, 16, r'$\mathbb{Q}(r)$ plus grand', 'limite', 's')
text(ax, 44, 2, '', 'encre') if False else None
save(fig, '63-179')
