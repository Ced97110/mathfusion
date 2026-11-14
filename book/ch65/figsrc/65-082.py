import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$t_1 = r_1r_2 + r_3r_4$', 'sujet', 'l')
xs = [14, 34, 54, 74]
for i, x in enumerate(xs):
    disc(ax, x, 42, 5.0, 'sujet', label=rf'$r_{i+1}={i+1}$', size='s')
def arcdown(x0, x1, y, h, role):
    pts = [(x0 + (x1 - x0) * t / 20, y - h * math.sin(math.pi * t / 20)) for t in range(21)]
    line(ax, pts, role, lw=1.1)
arcdown(14, 34, 36.5, 5, 'varie')
arcdown(54, 74, 36.5, 5, 'varie')
text(ax, 24, 27, r'$1 \times 2 = 2$', 'varie', 's')
text(ax, 64, 27, r'$3 \times 4 = 12$', 'varie', 's')
arrow(ax, (24, 24.5), (36, 16.5), 'fixe')
arrow(ax, (64, 24.5), (52, 16.5), 'fixe')
box(ax, 24, 4, 40, 12, 'resultat', label=r'$t_1 = 2 + 12 = 14$', size='m')
save(fig, '65-082')
