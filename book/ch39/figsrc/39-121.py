import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
ox, oy, u = 12, 6, 5.2
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox, oy), (ox + 4.2 * u, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox, oy + 12.2 * u), 'fixe', lw=0.7)
pts = [(2, 1, 'sujet'), (3, 4, 'varie'), (2, 11, 'resultat')]
for a, b, r in pts:
    q = P(a, b)
    line(ax, [(ox, oy), q], r, lw=0.8)
    disc(ax, q[0], q[1], 1.3, r)
text(ax, P(2, 1)[0] + 3, P(2, 1)[1] - 3.2, r'$2+i$', 'sujet', ha='left')
text(ax, P(3, 4)[0] + 2.5, P(3, 4)[1], r'$3+4i$', 'varie', ha='left')
text(ax, P(2, 11)[0] + 2.5, P(2, 11)[1], r'$2+11i$', 'resultat', ha='left')
arrow(ax, (P(2, 1)[0] - 1.5, P(2, 1)[1] + 2), (P(3, 4)[0] - 2, P(3, 4)[1] - 1), 'varie', curve=-0.3)
arrow(ax, (P(3, 4)[0] - 2, P(3, 4)[1] + 2), (P(2, 11)[0] - 2, P(2, 11)[1] - 2), 'varie', curve=-0.2)
text(ax, 24, 19, r'$\times\,(2+i)$', 'varie', ha='left')
text(ax, 24, 42, r'$\times\,(2+i)$', 'varie', ha='left')
text(ax, 46, 74, r'$(2+i)^2 = 3+4i$', 'varie', ha='left')
text(ax, 46, 66, r'$(3+4i)(2+i)=2+11i$', 'resultat', ha='left')
text(ax, 46, 58, r'$11i=\sqrt{-121}$', 'encre', ha='left')
text(ax, 46, 50, r'$2-i$ donne $2-11i$', 'autre', ha='left')
box(ax, 46, 4, 40, 9, 'resultat', label=r'$(2+i)+(2-i)=4$')
save(fig, '39-121')
