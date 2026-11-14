import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(58)
S = 5.0
X0 = 6.0

def cells(n, y, role):
    for i in range(n):
        ax.add_patch(Rectangle((X0 + S * i, y), S, S, fc=FILL[role], ec=COL[role], lw=0.6, zorder=2))

def group(k, size, y, role):
    ax.add_patch(Rectangle((X0 + S * k * size, y - 0.8), S * size, S + 1.6, fc='none', ec=COL[role], lw=1.6, zorder=3))

cells(12, 44, 'sujet')
for k in range(3): group(k, 4, 44, 'resultat')
text(ax, 36, 38, r'$12=4\times3$ : 3 groupes de 4', 'resultat', 's')
text(ax, 76, 46.5, r'$4\mid12$', 'resultat', 'm')
cells(12, 28, 'sujet')
for k in range(2): group(k, 6, 28, 'resultat')
text(ax, 36, 22, r'$12=6\times2$ : 2 groupes de 6', 'resultat', 's')
text(ax, 76, 30.5, r'$6\mid12$', 'resultat', 'm')
cells(4, 12, 'sujet')
group(0, 4, 12, 'resultat')
cells(2, 12, 'limite') if False else None
for i in range(4, 6):
    ax.add_patch(Rectangle((X0 + S * i, 12), S, S, fc=FILL['limite'], ec=COL['limite'], lw=0.6, zorder=2))
text(ax, 36, 6, 'reste 2 : 4 ne divise pas 6', 'limite', 's')
text(ax, 76, 14.5, r'$4\nmid6$', 'limite', 'm')
save(fig, '67-054')
