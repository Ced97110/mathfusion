import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'mêmes groupes', 'encre', 'm')
box(ax, 2, 44, 36, 12, 'sujet', label=r'$|G|=p^k$', size='m')
box(ax, 50, 44, 36, 12, 'autre', label=r'ordres = puissances de $p$', size='s')
arrow(ax, (39, 50), (49, 50), 'encre', both=True)
for y, g, ok in [(26, r'$\mathbb{Z}/8\mathbb{Z}$', True), (8, r'$\mathbb{Z}/6\mathbb{Z}$', False)]:
    role = 'resultat' if ok else 'limite'; w = 'oui' if ok else 'non'
    box(ax, 2, y, 36, 11, role, label=f'{g} : {w}', size='s')
    box(ax, 50, y, 36, 11, role, label=f'{g} : {w}', size='s')
    arrow(ax, (39, y + 5.5), (49, y + 5.5), role, both=True)
save(fig, '50-029')
