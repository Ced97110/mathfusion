import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
w, h, x0, y0 = 10, 8, 10, 24
vals = [[1, 0], [0, 1], [0, 0]]
for i, row in enumerate(vals):
    for j, v in enumerate(row):
        box(ax, x0 + j * w, y0 + (2 - i) * h, w, h, 'sujet', label=str(v))
text(ax, 5, y0 + 12, '3 lignes', 'varie', 's', rot=90)
text(ax, x0 + w, 19, '2 colonnes', 'varie', 's')
text(ax, 36, 44, 'colonnes de longueur 1', 'resultat', 's', ha='left')
text(ax, 36, 39.5, 'et perpendiculaires', 'resultat', 's', ha='left')
text(ax, 36, 32, '(3, 4) → (3, 4, 0)', 'encre', 's', ha='left')
text(ax, 36, 22, 'pas carrée : pas d’inverse', 'limite', 's', ha='left')
save(fig, '73-083')
