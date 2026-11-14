import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cols = [12, 34, 56, 78]
heads = ['partir de $d$', 'retirer 1', 'la moitié', 'arrondir : $t$']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
data = [(34, ['5', '4', '2', '2']), (14, ['4', '3', '1,5', '1'])]
for c, h in zip(cols, heads):
    text(ax, c, 50, h, 'fixe', 's')
for y, vals in data:
    for i, (c, v) in enumerate(zip(cols, vals)):
        box(ax, c - 7, y - 5, 14, 10, roles[i], label=v, size='l')
        if i < 3:
            arrow(ax, (c + 7.5, y), (cols[i + 1] - 7.5, y), 'varie')
save(fig, '68-082')
