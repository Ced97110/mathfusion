import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(56)
f = numberline(ax, 10, 74, 28, 0, 0.02, step=0.005, arrow_right=False, size='s')
xp = f(0.01745)
disc(ax, xp, 28, 1.3, 'resultat')
box(ax, xp - 24, 42, 41, 10, 'autre', label=r'cercle : $2\pi \div 360$', size='s')
box(ax, xp - 24, 4, 41, 10, 'sujet', label=r'triangle : $\sin 1°$', size='s')
arrow(ax, (xp, 42), (xp, 30), 'autre')
arrow(ax, (xp, 14), (xp, 26), 'sujet')
text(ax, xp + 3, 33.5, '0,01745', 'resultat', 's', ha='left')
save(fig, '29-013')
