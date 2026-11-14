import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = lambda y: 6 + (y - 1811) * 76 / 35
line(ax, [(3, 34), (85, 34)], 'fixe', lw=1.0)
ev = [(1811, 'fixe'), (1829, 'varie'), (1832, 'limite'), (1846, 'resultat')]
for yr, role in ev:
    disc(ax, f(yr), 34, 1.6, role)
# au-dessus
box(ax, 2, 44, 27, 12, 'fixe')
text(ax, 15.5, 52, '1811', 'fixe', 'm', weight='bold'); text(ax, 15.5, 47, 'naissance', 'fixe', 's')
line(ax, [(f(1811), 35.8), (f(1811), 44)], 'fixe')
box(ax, 31, 44, 30, 12, 'varie')
text(ax, 46, 52, '1829 · 17 ans', 'varie', 'm', weight='bold'); text(ax, 46, 47, 'mémoires perdus', 'varie', 's')
line(ax, [(f(1829), 35.8), (f(1829), 44)], 'varie')
box(ax, 64, 44, 22, 12, 'resultat')
text(ax, 75, 52, '1846', 'resultat', 'm', weight='bold'); text(ax, 75, 47, 'publication', 'resultat', 's')
line(ax, [(f(1846), 35.8), (f(1846), 44)], 'resultat')
# au-dessous
box(ax, 30, 6, 34, 12, 'limite')
text(ax, 47, 14, '1832 · 20 ans', 'limite', 'm', weight='bold'); text(ax, 47, 9, 'mort en duel', 'limite', 's')
line(ax, [(f(1832), 32.2), (f(1832), 18)], 'limite')
brace(ax, f(1832), f(1846), 30, 'resultat', label='14 ans')
save(fig, '64-010')
