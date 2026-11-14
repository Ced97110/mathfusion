import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = (10, 12)
def P(r, d): return (c[0] + r * math.cos(math.radians(d)), c[1] + r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=40): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
R = 40
poly(ax, [c] + arc(R, 0, 30, 20), 'sujet')
poly(ax, [c] + arc(R, 30, 90, 40), 'fixe')
for d in (0, 30, 60, 90):
    line(ax, [c, P(R, d)], 'fixe', lw=0.8)
line(ax, [c, P(R + 8, 90)], 'fixe', lw=1.2, dash=True)
arrow(ax, c, P(30, 30), 'sujet', lw=1.5)
text(ax, P(26, 15)[0] + 2, P(26, 15)[1] - 5, '30°', 'sujet', 's')
text(ax, P(26, 45)[0] - 1, P(26, 45)[1] + 3, '30°', 'fixe', 's')
text(ax, P(26, 75)[0] - 2, P(26, 75)[1] + 2, '30°', 'fixe', 's')
text(ax, P(R + 8, 90)[0] + 3, P(R + 8, 90)[1] - 1, 'θ = 90°', 'fixe', 's', ha='left')
text(ax, P(30, 30)[0] + 2, P(30, 30)[1] + 2, '$z_0$', 'sujet', 's', ha='left')
box(ax, 52, 24, 34, 11, 'sujet', label='θ ÷ n = 90° ÷ 3 = 30°', size='s')
text(ax, 69, 16, 'angle de départ de $z_0$', 'sujet', 's')
text(ax, 69, 45, 'n = 3 parts égales', 'fixe', 's')
save(fig, '39-091')
