import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
c = (30, 36); s = 12.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=60): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
arrow(ax, (c[0] - 31, c[1]), (c[0] + 31, c[1]), 'fixe', lw=0.6)
arrow(ax, (c[0], c[1] - 31), (c[0], c[1] + 31), 'fixe', lw=0.6)
line(ax, arc(2, 0, 360), 'sujet', lw=1.3)
for d in (0, 120, 240):
    line(ax, [c, P(2, d)], 'sujet', lw=1.0)
    disc(ax, *P(2, d), 1.5, 'sujet')
text(ax, P(2, 0)[0] + 3, P(2, 0)[1] + 3.5, '$z_0$', 'sujet', 's')
text(ax, P(2, 120)[0] - 4, P(2, 120)[1] + 3, '$z_1$', 'sujet', 's')
text(ax, P(2, 240)[0] - 4, P(2, 240)[1] - 3, '$z_2$', 'sujet', 's')
text(ax, c[0] - 3, c[1] - 3, 'O', 'fixe', 's')
box(ax, 60, 44, 26, 12, 'sujet', label='$\\sqrt[3]{8}$ = 2', size='m')
text(ax, 73, 36, 'même distance', 'sujet', 's')
text(ax, 73, 31.5, 'pour toutes', 'sujet', 's')
text(ax, 73, 27, 'les racines', 'sujet', 's')
save(fig, '39-090')
