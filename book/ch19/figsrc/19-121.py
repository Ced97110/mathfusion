import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(58); P = plane(ax, 14, 8, 8, 8, 0, 6, 0, 5)
line(ax, [P(4, -0.3), P(4, 5.2)], 'sujet', lw=1.6)
for y in (0, 4):
    disc(ax, *P(4, y), 1.3, 'sujet')
    text(ax, P(4, y)[0] - 3, P(4, y)[1], f'(4, {y})', 'sujet', 's', ha='right')
text(ax, P(4, 0)[0], 3.8, '4', 'sujet', 's')
arrow(ax, (P(4.7, 0.3)), (P(4.7, 3.7)), 'varie', both=True)
text(ax, P(4.7, 2)[0] + 2, P(4.7, 2)[1], r'$y$ change', 'varie', 's', ha='left')
text(ax, P(4, 5.2)[0] + 3, P(4, 5.2)[1] + 1, r'$x=4$', 'sujet', 'l', ha='left', weight='bold')
text(ax, 20, 52, r'$x$ reste 4', 'fixe', 'm')
save(fig, '19-121')
