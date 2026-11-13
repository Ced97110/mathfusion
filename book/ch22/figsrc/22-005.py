import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
a, b, c0 = 1.999396, 2.0, 2.002225
x0, x1 = 12, 74
f = lambda v: x0 + (v - a) / (c0 - a) * (x1 - x0)
arrow(ax, (4, 22), (86, 22), 'fixe', lw=0.9)
for v, role, top, bot in ((a, 'sujet', '1,414 × 1,414', '1,999396'), (b, 'resultat', None, '2'), (c0, 'varie', '1,415 × 1,415', '2,002225')):
    disc(ax, f(v), 22, 1.4, role)
    text(ax, f(v), 16.5, bot, role, 's')
    if top: text(ax, f(v), 28, top, role, 's')
text(ax, f(b), 28, 'l\'aire', 'resultat', 's')
text(ax, f(a) + 2, 10, 'trop petit', 'sujet', 's', ha='left')
text(ax, f(c0), 10, 'trop grand', 'varie', 's', ha='right')
text(ax, 44, 40, 'aucune décimale ne tombe sur 2', 'encre', 'm')
save(fig, '22-005')
