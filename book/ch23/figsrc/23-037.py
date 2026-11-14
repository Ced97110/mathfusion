import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(48, '5 + 3', ['8']), (32, '5 − 3', ['2']), (14, '5 ± 3', ['8', '2'])]
for y, e, rs in rows:
    box(ax, 6, y, 26, 10, 'sujet' if '±' in e else 'fixe', label=e)
    xs = [48] if len(rs) == 1 else [48, 66]
    for x, r in zip(xs, rs):
        arrow(ax, (33, y + 5), (x - 1, y + 5), 'varie') if x == 48 else arrow(ax, (33, y + 10), (x + 7, y + 10.6), 'varie', curve=-0.3)
        box(ax, x, y, 14, 10, 'resultat', label=r)
text(ax, 74, 53, 'un résultat', 'fixe', 's'); text(ax, 74, 37, 'un résultat', 'fixe', 's')
brace(ax, 48, 80, 13, 'resultat', label='deux réponses')
save(fig, '23-037')
