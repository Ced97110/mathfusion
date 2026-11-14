import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, s = 44, 36, 8.0
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(-4.6, 0), P(4.6, 0), 'fixe', lw=0.7)
arrow(ax, P(0, -3.6), P(0, 3.6), 'fixe', lw=0.7)
text(ax, 13, 39.5, 'axe horizontal', 'fixe', 's')
text(ax, 62, 71, 'axe vertical', 'fixe', 's')
# demi-tour : arc de P0 à P2 autour de l'origine
r = math.hypot(3, 2) * s
a0 = math.atan2(2, 3)
pts = [(ox + r * math.cos(a0 + math.pi * i / 30), oy + r * math.sin(a0 + math.pi * i / 30)) for i in range(31)]
line(ax, pts[:-1], 'resultat', lw=0.9, dash=True)
arrow(ax, pts[-2], pts[-1], 'resultat', lw=0.9)
text(ax, 20, 66, 'demi-tour', 'resultat', 's')
# deux reflets
arrow(ax, P(3, 2), P(3, -2), 'varie', lw=1.3)
arrow(ax, P(3, -2), P(-3, -2), 'varie', lw=1.3)
for (x, y), role in (((3, 2), 'sujet'), ((3, -2), 'varie'), ((-3, -2), 'resultat')):
    disc(ax, P(x, y)[0], P(x, y)[1], 1.4, role)
text(ax, P(3, 2)[0] + 7, P(3, 2)[1] + 2, r'$\langle 3,\ 2\rangle$', 'sujet', 's')
text(ax, P(3, -2)[0] + 6, P(3, -2)[1] - 3, r'$\langle 3,\ -2\rangle$', 'varie', 's')
text(ax, P(-3, -2)[0] - 2, P(-3, -2)[1] - 4.5, r'$\langle -3,\ -2\rangle$', 'resultat', 's')
text(ax, 80, 36 + 8, 'reflet 1', 'varie', 's')
text(ax, 44, 10, 'reflet 2', 'varie', 's')
save(fig, '41-166')
