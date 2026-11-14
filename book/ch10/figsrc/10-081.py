import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y0, k = 8, 1.0
for i, (v, r) in enumerate([(14, 10), (24, 20), (34, 30), (44, 40)]):
    x = 6 + 20 * i
    box(ax, x, y0, 7, v * k, 'sujet', r=0.3)
    box(ax, x + 7, y0, 7, r * k, 'varie', r=0.3)
    arrow(ax, (x + 10.5, y0 + r * k), (x + 10.5, y0 + v * k), 'fixe', both=True, lw=0.7)
    text(ax, x + 14.5, y0 + (v + r) * k / 2 + 0, '4', 'fixe', 's', ha='left') if False else text(ax, x + 14.5, y0 + (v + r) * k / 2, '4', 'fixe', 's', ha='left')
    text(ax, x + 7, y0 - 3, str(v), 'sujet', 's')
box(ax, 6, 58, 6, 4, 'sujet', r=0.3); text(ax, 14, 60, 'vraie', 'sujet', 's', ha='left')
box(ax, 34, 58, 6, 4, 'varie', r=0.3); text(ax, 42, 60, 'arrondie', 'varie', 's', ha='left')
text(ax, 74, 60, r'$E=-16$', 'encre', 'm')
line(ax, [(4, y0), (84, y0)], 'fixe')
save(fig, '10-081')
