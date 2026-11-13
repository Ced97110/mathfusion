import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 49, 'Ludwig Sylow', 'sujet', 'l')
X = lambda v: 10 + (v - 1832) / 66 * 68
line(ax, [(6, 24), (84, 24)], 'fixe', lw=1.2)
ax.add_patch(Rectangle((X(1872), 22.2), X(1898) - X(1872), 3.6, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
text(ax, (X(1872) + X(1898)) / 2, 24, 'lycée', 'varie', 's')
for v, role in [(1832, 'fixe'), (1872, 'sujet'), (1898, 'resultat')]:
    disc(ax, X(v), 24, 1.8, role); text(ax, X(v), 15, str(v), role, 'm')
text(ax, X(1832), 33, 'naissance', 'fixe', 's')
text(ax, X(1872), 34, 'article de\n10 pages', 'sujet', 's')
text(ax, X(1898) - 2, 34, "chaire à\nl'université", 'resultat', 's')
brace(ax, X(1872), X(1898), 11, 'varie', label='26 ans', size='s')
save(fig, '50-010')
