import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
def bar(y, n, k, role):
    for i in range(n): box(ax, 4 + i * 60 / n, y, 60 / n, 8, role if i < k else 'fixe', fill=i < k, r=0.2, lw=0.5)
bar(40, 6, 1, 'sujet'); bar(26, 12, 2, 'resultat'); bar(12, 12, 1, 'limite')
text(ax, 67, 44, r'$\frac{1}{6}$', 'sujet', ha='left'); text(ax, 67, 30, r'$\frac{2}{12}$ juste', 'resultat', 's', ha='left'); text(ax, 67, 16, r'$\frac{1}{12}$ faux', 'limite', 's', ha='left')
text(ax, 34, 37, r'haut et bas $\times 2$ : même valeur', 'varie', 's')
text(ax, 34, 23, r'bas $\times 2$, haut pareil : moitié', 'varie', 's')
save(fig, '21-080')
