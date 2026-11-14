import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, u = 44, 36, 6.4
line(ax, [(cx - 5.2 * u, cy), (cx + 5.4 * u, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - 5.2 * u), (cx, cy + 5.4 * u)], 'fixe', lw=0.5)
for r in range(1, 5):
    disc(ax, cx, cy, r * u, 'fixe', fill=False, lw=0.7)
    text(ax, cx - r * u, cy - 3, str(r), 'fixe', 's')
disc(ax, cx, cy, 5 * u, 'sujet', fill=False, lw=1.4)
P = (cx + 3 * u, cy + 4 * u); Q = (cx + 5 * u, cy)
line(ax, [(cx, cy), P], 'sujet', lw=1.0); line(ax, [(cx, cy), Q], 'sujet', lw=1.0)
disc(ax, *P, 1.6, 'sujet'); disc(ax, *Q, 1.6, 'sujet'); disc(ax, cx, cy, 1.4, 'encre')
text(ax, P[0] + 1, P[1] + 4, r'$P(3,\,4)$', 'sujet', 'm')
text(ax, Q[0] - 2, Q[1] - 4.5, r'$Q(5,\,0)$', 'sujet', 'm')
text(ax, cx - 3, cy + 3, r'$O$', 'encre', 'm')
text(ax, (cx + P[0]) / 2 - 3, (cy + P[1]) / 2 + 2, '5', 'sujet', 'm')
text(ax, 44, 77, 'même distance : même cercle', 'sujet', 's')
save(fig, '43-127')
