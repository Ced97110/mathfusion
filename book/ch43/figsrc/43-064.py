import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 89, r'$\bar{a}\;=\;\{\,b\in S\;\mid\;b\,E\,a\,\}$', 'encre', 'l')
rows = [(r'$\bar{a}$', 'classe de $a$', 'sujet'), (r'$\{\ \}$', 'l’ensemble des', 'autre'),
        (r'$b\in S$', 'b est un élément de S', 'fixe'), (r'$\mid$', 'tels que', 'varie'),
        (r'$b\,E\,a$', 'b est en relation avec a', 'resultat')]
for k, (sym, mean, role) in enumerate(rows):
    y = 72 - 14 * k
    box(ax, 10, y - 5, 26, 10, role, label=sym)
    arrow(ax, (37.5, y), (44, y), role)
    text(ax, 47, y, mean, role, 'm', ha='left')
save(fig, '43-064')
