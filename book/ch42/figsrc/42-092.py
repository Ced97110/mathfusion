import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k, s = 8.0, 2.2; x0 = 44; y0 = 26
line(ax, [(4, y0), (84, y0)], 'fixe', lw=1.0)
xs = [i / 20 for i in range(-80, 81)]
line(ax, [(x0 + x * k, y0 + x * x * s) for x in xs], 'fixe', lw=1.2)
for x in (-2, 3):
    disc(ax, x0 + x * k, y0 + x * x * s, 1.6, 'resultat')
    text(ax, x0 + x * k, y0 - 4, f'{x} → {x*x}'.replace('-', '−'), 'resultat', 's')
disc(ax, x0, y0, 2.2, 'limite')
text(ax, x0, y0 - 4, '0 → 0', 'limite', 's')
box(ax, 14, 6, 60, 9, 'limite', label='x = 0 : 0² = 0, pas > 0', size='s')
text(ax, 44, 68, 'x² > 0 pour tout x : faux', 'limite', 'm', weight='bold')
save(fig, '42-092')
