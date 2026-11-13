import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
k = 0.9
for y, lab, res, role, wd, v in [(40, 'virgule : × 10', '30 po', 'limite', 30 * k, 'x'), (20, 'facteur : × 12', '36 po', 'resultat', 36 * k, 'x')]:
    box(ax, 2, y, 22, 10, 'fixe', label='3 pieds')
    arrow(ax, (26, y + 5), (50, y + 5), 'varie')
    text(ax, 38, y + 9.5, lab, 'varie', 's')
    box(ax, 52, y, wd, 10, role, label=res)
text(ax, 44, 8, 'la virgule fait perdre 6 po', 'limite', 's')
text(ax, 44, 58, '1 pied = 12 po, pas 10', 'encre', 's')
save(fig, '11-046')
