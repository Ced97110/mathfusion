import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'trace nulle : jamais de base', 'limite', 'm')
text(ax, 22, 64, 'conjugués', 'encre', 's')
text(ax, 49, 64, 'trace', 'encre', 's')
text(ax, 71, 64, 'verdict', 'encre', 's')
rows = [(50, r'$\alpha,\ \alpha^{2},\ \alpha^{2}+\alpha$', r'$T=0$', 'liés : pas de base', 'limite'),
        (33, r'$\alpha+1,\ \alpha^{2}+1,\ \alpha^{2}+\alpha+1$', r'$T=1$', 'base normale', 'resultat'),
        (16, '1, 1, 1', r'$T=1$', 'pas une base', 'limite')]
for y, conj, tr, ver, role in rows:
    box(ax, 2, y - 6, 41, 12, 'sujet', label=conj, size='s')
    disc(ax, 49.5, y, 5, 'fixe', label=tr, size='s')
    box(ax, 57, y - 6, 29, 12, role, label=ver, size='s')
save(fig, '67-193')
