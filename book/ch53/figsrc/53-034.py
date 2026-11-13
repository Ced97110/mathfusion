import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# L, b=3 : 11 -> 14 -> 14 -> O ; Y, b=5 : 24 -> 29 -> 3 -> D
bw, gap, x0 = 17.0, 5.0, 2.5
xs = [x0 + i * (bw + gap) for i in range(4)]
heads = ['numéro $p$', 'ajouter $b$', 'reste ÷ 26', 'lettre']
for x, h in zip(xs, heads):
    text(ax, x + bw / 2, 52, h, 'fixe', 's')
rows = [(30, ['L : 11', '+3 : 14', '14', 'O']), (8, ['Y : 24', '+5 : 29', '3', 'D'])]
roles = ['sujet', 'varie', 'varie', 'resultat']
for y, cells in rows:
    for i, (x, c) in enumerate(zip(xs, cells)):
        box(ax, x, y, bw, 11, roles[i], label=c, weight='bold' if i == 3 else 'normal')
        if i < 3: arrow(ax, (x + bw + 0.4, y + 5.5), (x + bw + gap - 0.4, y + 5.5), 'fixe')
save(fig, '53-034')
