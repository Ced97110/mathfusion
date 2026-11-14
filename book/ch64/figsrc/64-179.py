import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
sx, x0, y0 = 10.9, 44, 38
roots = [-2.9859, -0.1108, 3.0137]
im = 1.7340
arrow(ax, (3, y0), (85, y0), 'fixe', lw=0.7)
text(ax, 44, 73, 'conjugaison complexe', 'varie', 'm', weight='bold')
for k, r in enumerate(roots):
    disc(ax, x0 + sx * r, y0, 1.6, 'fixe')
    text(ax, x0 + sx * r + (-3.5 if k == 1 else 0), y0 - 5, f'$r_{k + 1}$', 'fixe', 'm')
p4, p5 = (x0 + sx * 0.0415, y0 + 11 * im), (x0 + sx * 0.0415, y0 - 11 * im)
disc(ax, *p4, 1.6, 'varie'); disc(ax, *p5, 1.6, 'varie')
text(ax, p4[0] - 5, p4[1], '$r_4$', 'varie', 'm'); text(ax, p5[0] - 5, p5[1], '$r_5$', 'varie', 'm')
arrow(ax, (p4[0] + 7, p4[1] - 1), (p5[0] + 7, p5[1] + 1), 'varie', both=True)
text(ax, p4[0] + 10, y0 + 3.5, '$(r_4\\ r_5)$', 'varie', 'm', ha='left')
text(ax, 44, 12, r'$r_1,\ r_2,\ r_3$ restent en place', 'fixe', 'm')
save(fig, '64-179')
