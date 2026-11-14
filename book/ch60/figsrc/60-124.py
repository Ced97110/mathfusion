import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
bx, bw, bh = 24, 62, 11
ys = [78, 59, 40]
steps = ['ordre de 1 : 12 = 4 × 3', '12 ÷ 4 = 3   et   12 ÷ 3 = 4', r'Bézout : $3 \times (-1) + 4 \times 1 = 1$']
tags = ['factoriser', 'diviser', 'Bézout']
for y, s, t in zip(ys, steps, tags):
    box(ax, bx, y, bw, bh, 'sujet', label=s, size='s')
    text(ax, 12, y + bh / 2, t, 'varie', 's')
for y in ys[:2]:
    arrow(ax, (bx + bw / 2, y - 0.4), (bx + bw / 2, y - 7.6), 'varie')
text(ax, 12, 34, 'multiplier', 'varie', 's')
text(ax, 12, 30.5, 'par 1', 'varie', 's')
box(ax, 4, 14, 38, 14, 'resultat', label='9 : ordre 4', size='s')
box(ax, 46, 14, 38, 14, 'resultat', label='4 : ordre 3', size='s')
text(ax, 44, 8, '1 = 9 + 4', 'resultat', 'm', weight='bold')
arrow(ax, (40, 39.6), (26, 28.8), 'varie')
arrow(ax, (68, 39.6), (65, 28.8), 'varie')
save(fig, '60-124')
