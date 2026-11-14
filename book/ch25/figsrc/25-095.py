import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
ox, oy = 12, 12; sx = 70 / 90; sy = 5.5
X = lambda a: ox + a * sx
Y = lambda v: oy + v * sy
arrow(ax, (ox, oy), (86, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy), (ox, 80), 'fixe', lw=0.9)
line(ax, [(X(90), oy), (X(90), 80)], 'limite', lw=1.4)
pts = [(X(a / 2), Y(math.tan(math.radians(a / 2)))) for a in range(0, 171)]
line(ax, pts, 'sujet', lw=1.5)
for a, v in [(45, 1.0), (60, 1.73)]:
    line(ax, [(X(a), oy), (X(a), Y(v)), (ox, Y(v))], 'fixe', dash=True, lw=0.6)
    disc(ax, X(a), Y(v), 1.3, 'varie')
text(ax, X(45) - 1, oy - 3.5, '45°', 'varie', 'm', weight='bold')
text(ax, X(60) + 2, oy - 3.5, '60°', 'varie', 'm', weight='bold')
for v in (5, 10):
    line(ax, [(ox - 1, Y(v)), (ox + 1, Y(v))], 'fixe', lw=0.8); text(ax, ox - 4, Y(v), str(v), 'fixe', 's')
line(ax, [(ox - 1, Y(1)), (ox + 1, Y(1))], 'varie', lw=0.8); line(ax, [(ox - 1, Y(1.73)), (ox + 1, Y(1.73))], 'varie', lw=0.8)
text(ax, ox - 4, Y(1) - 1.5, '1', 'varie', 'm', weight='bold')
text(ax, ox - 5.5, Y(1.73) + 2.2, '1,73', 'varie', 'm', weight='bold')
text(ax, X(90), oy - 3.5, '90°', 'limite', 's')
text(ax, X(90) - 3, 82.5, 'verticale de 90°', 'limite', 's', ha='right')
text(ax, ox + 2, 82.5, r'$\tan A$', 'sujet', 'm', ha='left')
text(ax, 84, oy - 3.5, r'$A$', 'fixe', 'm', ha='right') if False else None
save(fig, '25-095')
