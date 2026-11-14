import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(50)
box(ax, 4, 34, 54, 9, 'varie', label="l'angle dont la tangente est", size='s')
box(ax, 62, 34, 22, 9, 'fixe', label='0,9')
box(ax, 4, 10, 54, 9, 'sujet', label='arctan')
box(ax, 62, 10, 22, 9, 'fixe', label='0,9')
arrow(ax, (31, 33.5), (31, 19.5), 'varie'); text(ax, 35, 26.5, 'se raccourcit', 'varie', 's', ha='left')
arrow(ax, (73, 33.5), (73, 19.5), 'fixe'); text(ax, 71, 26.5, 'pareil', 'fixe', 's', ha='right')
text(ax, 44, 3.5, 'la machine donne : ≈ 41,987°', 'resultat', 's')
save(fig, '25-078')
