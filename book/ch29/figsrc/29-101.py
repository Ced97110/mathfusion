import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(70)
C = (24, 40); R = 18
disc(ax, C[0], C[1], R, 'sujet', lw=0.8)
ax.add_patch(Circle(C, R, fc='none', ec=COL['varie'], lw=2.4, zorder=3))
line(ax, [C, (C[0] + R, C[1])], 'sujet', lw=1.4)
text(ax, 33, 43, r'$r = 5$ cm', 'sujet', 's'); text(ax, 20, 32, r'$\theta = 2\pi$', 'sujet', 's')
text(ax, 69, 60, 'arc : le tour', 'varie'); text(ax, 69, 55, r'$s = 2\pi r$', 'varie'); text(ax, 69, 50, r'$\approx 31{,}4$ cm', 'varie')
arrow(ax, (51, 56), (36.4, 53), 'varie', lw=0.8)
text(ax, 69, 30, 'aire : le disque', 'sujet'); text(ax, 69, 25, r'$A = \pi r^2$', 'sujet'); text(ax, 69, 20, r'$\approx 78{,}5$ cm$^2$', 'sujet')
arrow(ax, (51, 26), (34, 35), 'sujet', lw=0.8)
text(ax, 44, 8, 'secteur d’un tour = disque', 'resultat')
save(fig, '29-101')
