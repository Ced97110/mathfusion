import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ox, oy, kx, ky = 46, 46, 30.0, 16.0; h = math.pi / 2
line(ax, [(ox - 38, oy), (ox + 38, oy)], 'fixe', lw=0.5); line(ax, [(ox, oy - 31), (ox, oy + 31)], 'fixe', lw=0.5)
xs = [-1 + 2 * i / 80 for i in range(81)]
line(ax, [(ox + x * kx, oy + math.asin(x) * ky) for x in xs], 'sujet', lw=1.8)
for x, lab, rl in ((-1, '−1', r'$-\pi/2$'), (0, '0', None), (1, '1', r'$\pi/2$')):
    P = (ox + x * kx, oy + math.asin(x) * ky); disc(ax, *P, 1.3, 'sujet')
    if x:
        line(ax, [(P[0], oy), P, (ox, P[1])], 'fixe', dash=True, lw=0.6)
        text(ax, P[0], oy + 3.5 if x < 0 else oy - 3.5, lab, 'fixe', 's')
        text(ax, ox - 2 if x > 0 else ox + 2, P[1], rl, 'sujet', 's', ha='right' if x > 0 else 'left')
arrow(ax, (ox - kx, 12), (ox + kx, 12), 'varie', lw=1.3); text(ax, ox, 7, 'x : de −1 à 1', 'varie', 'm')
arrow(ax, (ox + 34, oy - 20), (ox + 34, oy + 20), 'varie', lw=1.3); text(ax, ox + 38.5, oy, r'angle : de $-\pi/2$ à $\pi/2$', 'varie', 's', rot=90)
text(ax, ox - 18, oy + 17, 'arcsin', 'sujet', 'm')
text(ax, ox + 26, oy - 14, 'la courbe monte', 'sujet', 's') if False else None
save(fig, '33-076')
