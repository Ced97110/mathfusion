import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
bw, gap = 18, 2
x0 = (88 - (4 * bw + 3 * gap)) / 2
for b in range(4):
    bx = x0 + b * (bw + gap)
    box(ax, bx, 48, bw, 14, 'fixe')
    for i in range(5): disc(ax, bx + 3 + i * 3, 58, 1.2, 'sujet')
    for i in range(2): disc(ax, bx + 3 + i * 3, 52, 1.2, 'varie')
text(ax, 44, 67, 'par boîte : 4(5 + 2) = 28', 'encre', 'm')
arrow(ax, (44, 46), (44, 35), 'varie')
text(ax, 48, 40.5, 'on regroupe par sorte', 'varie', 's', ha='left')
for i in range(5):
    for j in range(4): disc(ax, 14 + i * 3, 19.5 + j * 3, 1.2, 'sujet')
for i in range(2):
    for j in range(4): disc(ax, 52 + i * 3, 19.5 + j * 3, 1.2, 'varie')
text(ax, 20, 12.5, 'crayons : 4 · 5', 'sujet', 's')
text(ax, 54, 12.5, 'stylos : 4 · 2', 'varie', 's')
text(ax, 44, 5, 'par sorte : 4·5 + 4·2 = 28', 'encre', 'm')
save(fig, '12-101')
