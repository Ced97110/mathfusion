import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 36; x0, y0 = 4, 12
poly(ax, [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)], 'fixe', lw=0.6)
poly(ax, [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s)], 'sujet')
line(ax, [(x0 + s - 3, y0), (x0 + s - 3, y0 + 3), (x0 + s, y0 + 3)], 'sujet', lw=0.7)
for t in (0.45, 0.55):
    line(ax, [(x0 + s * t, y0 - 1.2), (x0 + s * t, y0 + 1.2)], 'varie', lw=1.0)
    line(ax, [(x0 + s - 1.2, y0 + s * t), (x0 + s + 1.2, y0 + s * t)], 'varie', lw=1.0)
text(ax, x0 + s / 2, y0 - 4, '1', 'sujet', 'm')
text(ax, x0 + s + 3.5, y0 + s / 2, '1', 'sujet', 'm')
text(ax, x0 + 12, y0 + 3.5, '45°', 'sujet', 's')
text(ax, x0 + s - 8, y0 + s - 4.5, '45°', 'sujet', 's')
box(ax, 50, 42, 36, 10, 'sujet', label='côtés égaux : 1 et 1', size='s')
arrow(ax, (68, 42), (68, 36), 'varie')
box(ax, 50, 26, 36, 10, 'varie', label='angles aigus égaux', size='s')
arrow(ax, (68, 26), (68, 20), 'varie')
box(ax, 50, 10, 36, 10, 'resultat', label=r'$90° \div 2 = 45°$', size='m')
save(fig, '25-085')
