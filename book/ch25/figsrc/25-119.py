import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(66)
O = (18, 38); k = 6
line(ax, [O, (O[0] + 4 * k, O[1] + 3 * k)], 'sujet', lw=1.4)
line(ax, [O, (O[0] + 3 * k, O[1] - 4 * k)], 'autre', lw=1.4)
line(ax, [(O[0] + 2.4, O[1] + 1.8), (O[0] + 2.4 + 1.8, O[1] + 1.8 - 2.4), (O[0] + 1.8, O[1] - 2.4)], 'fixe')
text(ax, 44, 60, 'pente 0,75', 'sujet', 'm', ha='left')
text(ax, 40, 14, 'pente −4/3', 'autre', 'm', ha='left')
text(ax, 8, 50, 'perpendiculaires', 'fixe', 's', ha='left')
box(ax, 4, 4, 30, 9, 'resultat', label='0,75 × (−4/3)', size='s')
text(ax, 62, 8.5, '= −1', 'resultat', 'l', weight='bold')
save(fig, '25-119')
