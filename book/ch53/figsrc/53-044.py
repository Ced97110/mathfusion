import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# a = 5, b = 3 : E 4 -> 20 -> 23 -> X ; Y 24 -> 120 -> 123 -> 19 (T)
bw, gap, x0 = 13.0, 4.0, 2.0
xs = [x0 + i * (bw + gap) for i in range(5)]
heads = ['$p$', r'$\times 5$', '$+3$', 'mod 26', '']
for x, h in zip(xs, heads):
    if h: text(ax, x + bw / 2, 52, h, 'fixe', 'm')
rows = [(30, ['E : 4', '20', '23', '23', 'X']), (8, ['Y : 24', '120', '123', '19', 'T'])]
roles = ['sujet', 'varie', 'varie', 'varie', 'resultat']
for y, cells in rows:
    for i, (x, c) in enumerate(zip(xs, cells)):
        box(ax, x, y, bw, 11, roles[i], label=c, weight='bold' if i == 4 else 'normal')
        if i < 4: arrow(ax, (x + bw + 0.3, y + 5.5), (x + bw + gap - 0.3, y + 5.5), 'fixe')
save(fig, '53-044')
