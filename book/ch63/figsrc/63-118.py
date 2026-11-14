import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 10, 46, 50, 'fixe', fill=False, dash=True)
text(ax, 25, 65, '4 corps plus petits que $E$', 'fixe', 's')
cells = [(4, 36, r'$\mathbb{Q}$'), (26, 36, r'$\mathbb{Q}(\sqrt{3})$'), (4, 16, r'$\mathbb{Q}(\sqrt{5})$'), (26, 16, r'$\mathbb{Q}(\sqrt{15})$')]
for x, y, l in cells:
    box(ax, x, y, 20, 12, 'fixe', label=l, size='s')
box(ax, 56, 38, 30, 16, 'resultat', label=r'$E=\mathbb{Q}(\gamma)$', size='s')
box(ax, 56, 12, 30, 16, 'varie', label=r'$\gamma=\sqrt{3}+\sqrt{5}$', size='s')
arrow(ax, (71, 28), (71, 38), 'resultat')
text(ax, 71, 62, 'engendre tout', 'resultat', 's')
text(ax, 25, 4, r'$\gamma$ n’est dans aucun des 4', 'limite', 's')
save(fig, '63-118')
