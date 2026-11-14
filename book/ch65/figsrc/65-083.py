import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$t_2 = r_1r_3 + r_2r_4$', 'sujet', 'l')
xs = [14, 34, 54, 74]
vals = [2, 3, 5, 7]
for i, x in enumerate(xs):
    disc(ax, x, 40, 5.0, 'sujet', label=rf'$r_{i+1}={vals[i]}$', size='s')
def arc(x0, x1, y, h, role, up):
    pts = [(x0 + (x1 - x0) * t / 20, y + (h if up else -h) * math.sin(math.pi * t / 20)) for t in range(21)]
    line(ax, pts, role, lw=1.1)
arc(14, 54, 45.5, 8, 'varie', True)
arc(34, 74, 34.5, 8, 'autre', False)
text(ax, 34, 58, r'$2 \times 5 = 10$', 'varie', 's')
text(ax, 54, 22, r'$3 \times 7 = 21$', 'autre', 's')
box(ax, 22, 3, 44, 12, 'resultat', label=r'$t_2 = 10 + 21 = 31$', size='m')
arrow(ax, (54, 19.5), (54, 16), 'fixe')
save(fig, '65-083')
