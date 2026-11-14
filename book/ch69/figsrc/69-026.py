import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'une seule des trois relations est vraie', 'resultat', 's')
rows = [(40, '7 − 4 = 3 ∈ P', ['7 > 4', '7 = 4', '4 > 7'], 0),
        (24, '5 − 5 = 0', ['5 > 5', '5 = 5', '5 > 5'], 1),
        (8, '2 − 6 = −4 ; 4 ∈ P', ['2 > 6', '2 = 6', '6 > 2'], 2)]
cw, x0 = 14.5, 38
for y, d, rel, ok in rows:
    text(ax, 2, y + 5, d, 'varie', 's', ha='left')
    for k, r in enumerate(rel):
        role = 'resultat' if k == ok else 'limite'
        box(ax, x0 + k * (cw + 1.5), y, cw, 10, role, label=r, size='s')
save(fig, '69-026')
