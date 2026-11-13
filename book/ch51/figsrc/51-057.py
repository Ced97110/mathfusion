import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'produits de 2 par un entier', 'varie', 'm')
f = numberline(ax, 8, 70, 22, -2, 4, role='fixe')
for v in (-2, 0, 2, 4):
    disc(ax, f(v), 33, 3.0, 'varie')
    line(ax, [(f(v), 30), (f(v), 24)], 'varie', lw=0.6, dash=True)
disc(ax, f(1), 33, 3.0, 'limite', fill=False, lw=1.0)
line(ax, [(f(1) - 1.8, 31.2), (f(1) + 1.8, 34.8)], 'limite', lw=1.2); line(ax, [(f(1) - 1.8, 34.8), (f(1) + 1.8, 31.2)], 'limite', lw=1.2)
line(ax, [(f(1), 30), (f(1), 24)], 'limite', lw=0.6, dash=True)
text(ax, f(1), 8, '1 : jamais obtenu', 'limite', 'm')
text(ax, f(1), 40.5, '', 'fixe') if False else None
save(fig, '51-057')
