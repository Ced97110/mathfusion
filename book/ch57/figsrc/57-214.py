import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 77, 'A : lignes 1 2 et 0 3\nB : lignes 1 0 et 1 1', 'encre', 'm')

def chain(cy, caption, ops, mids, end, endrole):
    text(ax, 3, cy + 10, caption, 'fixe', 's', ha='left')
    xs = [3, 35, 67]
    labels = ['(1 ; 0)'] + mids + [end]
    roles = ['sujet', 'fixe', endrole]
    for x, lab, role in zip(xs, labels, roles):
        box(ax, x, cy - 6, 15, 12, role, label=lab, size='s')
    for i, op in enumerate(ops):
        arrow(ax, (xs[i] + 15, cy), (xs[i + 1], cy), 'varie')
        text(ax, (xs[i] + 15 + xs[i + 1]) / 2, cy + 3, op, 'varie', 'm', weight='bold')

chain(54, 'B puis A : produit AB', ['B', 'A'], ['(1 ; 1)'], '(3 ; 3)', 'resultat')
chain(20, 'A puis B : produit BA', ['A', 'B'], ['(1 ; 0)'], '(1 ; 1)', 'autre')
text(ax, 44, 37, '≠', 'encre', 'xl', weight='bold')
save(fig, '57-214')
