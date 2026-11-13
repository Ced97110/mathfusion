import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
def mat(x0, vals, roles):
    pos = [(0, 8), (8, 8), (0, 0), (8, 0)]
    for (dx, dy), v, r in zip(pos, vals, roles):
        box(ax, x0 + dx, 20 + dy, 8, 8, r, label=v)
mat(3, ['1', '2', '0', '1'], ['fixe', 'varie', 'varie', 'fixe'])
mat(27, ['1', '0', '2', '1'], ['fixe', 'varie', 'varie', 'fixe'])
mat(66, ['1', '1', '1', '1'], ['resultat'] * 4)
arrow(ax, (45, 28), (64, 28), 'varie')
brace(ax, 3, 43, 18, 'varie', label='XY et YX : non symétriques')
text(ax, 74, 14, 'moyenne : symétrique', 'resultat', 's')
save(fig, '78-069')
