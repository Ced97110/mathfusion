import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def row(x0, y, n, role, sz=3.4, gap=1.0):
    for i in range(n):
        box(ax, x0 + i * (sz + gap), y, sz, sz, role, r=0.3)
text(ax, 22, 72, 'sommets', 'sujet', 'm', weight='bold')
text(ax, 66, 72, 'colorations', 'sujet', 'm', weight='bold')
line(ax, [(44, 5), (44, 76)], 'fixe', dash=True)
text(ax, 22, 62, r'$4 \div 4$', 'resultat', 'l')
text(ax, 66, 62, r'$16 \div 4$', 'limite', 'l')
text(ax, 22, 50, 'calculé', 'resultat', 's'); row(18, 42, 1, 'resultat', 4)
text(ax, 66, 50, 'calculé', 'limite', 's'); row(66 - 9.0, 42, 4, 'limite', 4, 1.0)
text(ax, 22, 32, 'réel', 'resultat', 's'); row(18, 24, 1, 'resultat', 4)
text(ax, 66, 32, 'réel', 'resultat', 's'); row(66 - 14.0, 24, 6, 'resultat', 4, 1.0)
text(ax, 22, 13, 'juste', 'resultat', 'l', weight='bold')
text(ax, 66, 13, 'faux', 'limite', 'l', weight='bold')
text(ax, 22, 6.5, '1 orbite', 'resultat', 's'); text(ax, 66, 6.5, '6 orbites, pas 4', 'limite', 's')
save(fig, '49-291')
