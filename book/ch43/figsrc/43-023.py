import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [(40, r'$\leq$', 'autre'), (57, 'écart ≤ 1', 'autre'), (76, 'équivalence', 'sujet')]
rows = ['réflexive', 'symétrique', 'transitive']
table = [[1, 0, 1], [1, 1, 0], [1, 1, 1]]  # columns: <=, ecart, equivalence -> per column below
cond = {0: (1, 0, 1), 1: (1, 1, 0), 2: (1, 1, 1)}
for ci, (x, h, role) in enumerate(cols):
    text(ax, x, 58, h, role, 's')
for ri, lab in enumerate(rows):
    y = 44 - ri*13
    text(ax, 3, y, lab, 'encre', 's', ha='left')
    for ci, (x, h, role) in enumerate(cols):
        if cond[ci][ri]: disc(ax, x, y, 3.2, 'resultat')
        else:
            disc(ax, x, y, 3.2, 'limite')
            line(ax, [(x-1.5, y-1.5), (x+1.5, y+1.5)], 'limite', lw=1.2); line(ax, [(x-1.5, y+1.5), (x+1.5, y-1.5)], 'limite', lw=1.2)
disc(ax, 8, 6, 2, 'resultat'); text(ax, 12, 6, 'condition vraie', 'resultat', 's', ha='left')
disc(ax, 50, 6, 2, 'limite'); text(ax, 54, 6, 'condition fausse', 'limite', 's', ha='left')
save(fig, '43-023')
