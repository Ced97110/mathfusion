import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def B(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
fig, ax = canvas(56)
B(ax, 4, 38, 26, 14, 'sujet', 'sec 35°', 'l')
text(ax, 17, 34.5, '= 1,2208', 'resultat', 'm')
arrow(ax, (30, 45), (42, 45), 'varie')
B(ax, 42, 38, 44, 14, 'autre', 'sécante de\ntrente-cinq degrés', 'm')
line(ax, [(4, 30.5), (86, 30.5)], 'fixe', dash=True)
for i, (a, b) in enumerate([('sec θ', 'sécante de thêta'), ('cosec θ', 'cosécante de thêta'), ('cotan θ', 'cotangente de thêta')]):
    y = 21 - i * 9.5
    B(ax, 4, y, 26, 8, 'sujet', a, 's'); arrow(ax, (30, y + 4), (42, y + 4), 'varie'); B(ax, 42, y, 44, 8, 'autre', b, 's')
save(fig, '31-038')
