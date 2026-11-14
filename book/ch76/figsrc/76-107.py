import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
M = [[2, 0, 1], [1, 3, 0], [0, 1, 4]]
fig, ax = canvas(62)
for r in range(3):
    for c in range(3):
        role = 'varie' if r == 0 else ('sujet' if c > 0 else 'fixe')
        box(ax, 6 + 9 * c, 48 - 9 * r, 9, 9, role, label=str(M[r][c]), size='m', r=0.4)
text(ax, 19.5, 24, r'1re ligne en orange', 'varie', 's')
box(ax, 44, 46, 40, 10, 'sujet', label=r'$2\times12=24$')
box(ax, 44, 34, 40, 10, 'fixe', label=r'$-\,0\times(\ldots)=0$')
box(ax, 44, 22, 40, 10, 'fixe', label=r'$+\,1\times1=1$')
box(ax, 44, 6, 40, 10, 'resultat', label=r'$\det A=25$', weight='bold')
arrow(ax, (34, 44), (43, 49), 'sujet')
save(fig, '76-107')
