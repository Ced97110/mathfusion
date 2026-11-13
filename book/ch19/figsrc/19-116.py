import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(56); P = plane(ax, 48, 10, 8, 8, -5, 4, 0, 4)
line(ax, [P(-4.8, 3), P(3.8, 3)], 'sujet', lw=1.6)
for x in (-4, 0, 2):
    line(ax, [P(x, 0), P(x, 3)], 'varie', dash=True)
    disc(ax, *P(x, 3), 1.2, 'sujet')
    text(ax, P(x, 0)[0] + (2 if x == 0 else 0), 6.5, str(x).replace('-', '−'), 'varie', 's')
arrow(ax, P(-4, 1.2), P(2, 1.2), 'varie', both=True)
text(ax, P(-1, 1.2)[0], P(-1, 1.2)[1] + 2.6, r'$x$ change', 'varie', 's')
text(ax, P(-2, 3)[0], P(-2, 3)[1] + 4, r'$y=3$', 'sujet', 'l', weight='bold')
text(ax, P(2.8, 3)[0], P(2.8, 3)[1] + 4, r'$y$ reste 3', 'fixe', 's')
save(fig, '19-116')
