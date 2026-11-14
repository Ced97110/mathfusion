import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, w5 = 24, 57.5
yt, yb = 40, 14
line(ax, [(x0, yt), (x0 + w5, yt)], 'sujet', lw=1.1); line(ax, [(x0, yb), (x0 + w5, yb)], 'varie', lw=1.1)
text(ax, 2, yt, 'pouces', 'sujet', 's', ha='left'); text(ax, 2, yb, 'centimètres', 'varie', 's', ha='left')
for i in range(6):
    x = x0 + i * w5 / 5
    r = 'resultat' if i == 5 else ('autre' if i == 1 else 'fixe')
    line(ax, [(x, yt - 1.5), (x, yt + 1.5)], 'sujet'); line(ax, [(x, yb - 1.5), (x, yb + 1.5)], 'varie')
    line(ax, [(x, yt - 2), (x, yb + 2)], r, dash=True)
for i, a, b in [(0, '0', '0'), (1, '1', '2,54'), (5, '5', '12,7')]:
    x = x0 + i * w5 / 5
    text(ax, x, yt + 4, a, 'sujet', 's'); text(ax, x, yb - 4, b, 'varie', 's')
text(ax, 44, 27, '1 pouce → 2,54 cm', 'autre', 's')
save(fig, '09-121')
