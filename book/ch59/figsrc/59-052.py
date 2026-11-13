import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
items = [('type I', 'ajoute', 'sujet', 'sujet', 'ligne 1', 'ligne 2', False, 64),
         ('type II', r'$\times(\pm1)$', 'sujet', 'autre', 'ligne 2', r'±ligne 2', False, 42),
         ('type III', 'échange', 'sujet', 'sujet', 'ligne 1', 'ligne 2', True, 20)]
for name, act, r1, r2, a, b, both, y in items:
    text(ax, 4, y + 5, name, 'encre', 'm', ha='left')
    box(ax, 28, y, 22, 10, r1, label=a)
    box(ax, 66, y, 20, 10, r2, label=b)
    arrow(ax, (51, y + 5), (65, y + 5), 'varie', lw=1.2, both=both)
    text(ax, 58, y + 9.5, act, 'varie', 's')
text(ax, 44, 6, 'chaque geste peut être défait', 'resultat', 'm')
save(fig, '59-052')
