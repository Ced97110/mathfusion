import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$t_3 = r_1r_4 + r_2r_3$', 'sujet', 'l')
xs = [14, 34, 54, 74]
for i, x in enumerate(xs):
    disc(ax, x, 40, 5.0, 'sujet', label=rf'$r_{i+1}={i+1}$', size='s')
def arc(x0, x1, y, h, role, up):
    pts = [(x0 + (x1 - x0) * t / 20, y + (h if up else -h) * math.sin(math.pi * t / 20)) for t in range(21)]
    line(ax, pts, role, lw=1.1)
arc(14, 74, 45.5, 10, 'varie', True)
arc(34, 54, 34.5, 6, 'autre', False)
text(ax, 44, 59, r'$1 \times 4 = 4$', 'varie', 's')
text(ax, 44, 24, r'$2 \times 3 = 6$', 'autre', 's')
box(ax, 22, 3, 44, 12, 'resultat', label=r'$t_3 = 4 + 6 = 10$', size='m')
save(fig, '65-084')
