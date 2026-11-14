import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
assert [n for n in (1, 2, 4) if n % 3 == 1] == [1, 4] and [n for n in (1, 11) if n % 3 == 1] == [1]
assert [n for n in (1, 3, 9) if n % 11 == 1] == [1]
def row(x0, yb, items):
    for i, (t, r) in enumerate(items): box(ax, x0 + 11 * i, yb, 9, 7, r, label=t, size='m')
text(ax, 3, 56, r'ordre 99 : $n_3$ divise 11', 'sujet', 's', ha='left')
row(3, 46, [('1', 'resultat'), ('11', 'limite')])
text(ax, 3, 39, r'ordre 99 : $n_{11}$ divise 9', 'sujet', 's', ha='left')
row(3, 29, [('1', 'resultat'), ('3', 'limite'), ('9', 'limite')])
text(ax, 47, 56, r'ordre 12 : $n_3$ divise 4', 'autre', 's', ha='left')
row(47, 46, [('1', 'varie'), ('2', 'limite'), ('4', 'varie')])
text(ax, 22, 18, '99 : un seul choix, abélien', 'resultat', 's', weight='bold')
text(ax, 66, 36, r'12 : deux choix, $A_4$ non abélien', 'limite', 's', weight='bold', ha='center')
text(ax, 44, 7, 'rouge : le reste n’est pas 1', 'limite', 's')
save(fig, '50-208')
