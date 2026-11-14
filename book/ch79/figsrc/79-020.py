import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx = [40, 59, 78]
for c, h in zip(cx, ['réflexivité', 'antisymétrie', 'transitivité']):
    text(ax, c, 53, h, 'fixe', 's')
for cy, h in zip([40, 28, 16], ['réels : taille', 'diviseurs de 60', 'parties de 3 stylos']):
    text(ax, 15, cy, h, 'encre', 's')
    for c in cx:
        box(ax, c - 8.5, cy - 5, 17, 10, 'resultat')
        line(ax, [(c - 2.7, cy), (c - 0.8, cy - 2.2), (c + 2.8, cy + 2.6)], 'resultat', lw=1.4)
brace(ax, 31.5, 86.5, 9, 'resultat', label='vraies dans les trois exemples')
save(fig, '79-020')
