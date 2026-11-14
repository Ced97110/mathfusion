import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 14, 54, 60, 12, 'fixe', label='ℤ² : couples à deux cases')
text(ax, 2, 39, 'sacs\ntypes', 'sujet', 's', ha='left')
text(ax, 2, 19, 'lots', 'autre', 's', ha='left')
for x, a in [(24, '(1, 0)'), (46, '(0, 1)')]:
    box(ax, x, 34, 18, 10, 'sujet', label=a, size='s')
for x, a in [(24, '(2, 1)'), (46, '(1, 1)')]:
    box(ax, x, 14, 18, 10, 'autre', label=a, size='s')
arrow(ax, (66, 39), (71, 36), 'resultat')
arrow(ax, (66, 19), (71, 32), 'resultat')
box(ax, 71, 24, 15, 20, 'resultat', label='rang\n2', size='s')
arrow(ax, (44, 54), (44, 46), 'fixe')
save(fig, '58-068')
