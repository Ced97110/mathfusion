import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k, s = 8.0, 2.2; x0 = 44; y0 = 26
poly(ax, [(4, y0), (84, y0), (84, 4), (4, 4)], 'limite')
text(ax, 44, 12, 'x² < 0 : jamais', 'limite', 's')
line(ax, [(4, y0), (84, y0)], 'fixe', lw=1.0)
xs = [i / 20 for i in range(-80, 81)]
line(ax, [(x0 + x * k, y0 + x * x * s) for x in xs], 'resultat', lw=1.4)
for x in (-3, 0, 3):
    disc(ax, x0 + x * k, y0 + x * x * s, 1.5, 'sujet')
    text(ax, x0 + x * k, y0 - 4, f'{x}'.replace('-', '−'), 'sujet', 's')
text(ax, 22, 56, '3² = 9', 'sujet', 's'); text(ax, 66, 56, '(−3)² = 9', 'sujet', 's')
text(ax, x0, 32, '0² = 0', 'sujet', 's')
text(ax, 44, 68, 'x² ≥ 0 pour tout x', 'resultat', 'm', weight='bold')
save(fig, '42-091')
