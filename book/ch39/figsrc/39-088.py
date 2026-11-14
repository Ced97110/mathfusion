import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
c = (28, 38); s = 11.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=60): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
line(ax, arc(2, 0, 360), 'fixe', dash=True)
arrow(ax, (c[0] - 27, c[1]), (c[0] + 27, c[1]), 'fixe', lw=0.6)
arrow(ax, (c[0], c[1] - 27), (c[0], c[1] + 27), 'fixe', lw=0.6)
for d in (0, 120, 240):
    line(ax, [c, P(2, d)], 'sujet', lw=1.0)
    disc(ax, *P(2, d), 1.6, 'sujet')
for d0, d1 in ((3, 117), (123, 237)):
    pts = arc(0.8, d0, d1); line(ax, pts, 'varie', lw=1.1); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.1)
text(ax, *P(1.45, 60), '+120°', 'varie', 's'); text(ax, *P(1.45, 180), '+120°', 'varie', 's')
text(ax, P(2, 0)[0] + 2.5, P(2, 0)[1] + 3.5, '$z_0$', 'sujet', 's')
text(ax, P(2, 120)[0] - 4.5, P(2, 120)[1] + 3, '$z_1$', 'sujet', 's')
text(ax, P(2, 240)[0] - 4.5, P(2, 240)[1] - 3, '$z_2$', 'sujet', 's')
box(ax, 54, 52, 32, 9, 'sujet', label='module : ∛8 = 2', size='s')
box(ax, 54, 38, 32, 9, 'fixe', label='départ : 0° ÷ 3 = 0°', size='s')
box(ax, 54, 24, 32, 9, 'varie', label='pas : 360° ÷ 3 = 120°', size='s')
text(ax, 70, 16, 'angles 0°, 120°, 240°', 'resultat', 's')
save(fig, '39-088')
