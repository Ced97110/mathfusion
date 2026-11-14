import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
ox, oy, s = 14, 22, 14.0
P = lambda k1, k2: (ox + k1 * s, oy + k2 * s)
# axes
arrow(ax, (ox - 2, oy), (ox + 3 * s + 8, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 2), (ox, oy + 3 * s + 8), 'fixe', lw=0.9)
text(ax, ox + 3 * s + 8, oy - 4, r'$k_1$', 'fixe', 'm')
text(ax, ox - 5, oy + 3 * s + 8, r'$k_2$', 'fixe', 'm')
# diagonale k1 = k2
line(ax, [P(0, 0), P(3.2, 3.2)], 'fixe', dash=True)
text(ax, P(3.2, 3.2)[0] + 1, P(3.2, 3.2)[1] + 2, r'$k_1=k_2$', 'fixe', 's', ha='left')
# droite des monômes de degré 3
line(ax, [P(3, 0), P(0, 3)], 'fixe', lw=0.6)
pts = [(3, 0, 'sujet'), (2, 1, 'sujet'), (1, 2, 'fixe'), (0, 3, 'fixe')]
for k1, k2, r in pts:
    x, y = P(k1, k2)
    disc(ax, x, y, 1.8, r)
    dx, dy = (3.5, 0) if (k1, k2) != (0, 3) else (3.5, 0)
    text(ax, x + 3.2, y + 2.4, f'({k1}, {k2})', r, 's', ha='left')
x0, y0 = P(3, 0); x1, y1 = P(2, 1)
arrow(ax, (x0 - 1.2, y0 + 1.6), (x1 + 1.2, y1 - 1.6), 'varie', lw=1.2)
text(ax, 53, 31, 'un pas', 'varie', 's', ha='left')
text(ax, 4, 8, 'gris : jamais le plus haut', 'fixe', 's', ha='left')
text(ax, 4, 2.5, 'bleu : peut être le plus haut', 'sujet', 's', ha='left')
save(fig, '55-093')
