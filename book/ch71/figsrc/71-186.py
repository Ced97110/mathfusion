import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 29, 45, 'diagonale', 'encre', 's'); text(ax, 59, 45, 'signature', 'encre', 's'); text(ax, 78, 45, '$p-q$', 'encre', 's')
rows = [(26, 'courbe 1', [('16', 'sujet'), ('4', 'sujet')], '(2, 0)', '2'),
        (6, 'courbe 2', [('6', 'sujet'), ('−2', 'varie')], '(1, 1)', '0')]
for y, lab, vs, sg, d in rows:
    text(ax, 2, y + 6, lab, 'encre', 's', ha='left')
    for i, (v, r) in enumerate(vs):
        box(ax, 16 + i * 13, y, 12, 12, r, label=v)
    arrow(ax, (42, y + 6), (50, y + 6), 'fixe')
    box(ax, 51, y, 16, 12, 'resultat', label=sg)
    text(ax, 78, y + 6, d, 'resultat', 'l', weight='bold')
text(ax, 22, 21, 'positif', 'sujet', 's'); text(ax, 22, 1.5, 'négatif', 'varie', 's')
save(fig, '71-186')
