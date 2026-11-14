import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 6.5
def plane(ox, three):
    oy = 30
    P = lambda a, b: (ox + a * u, oy + b * u)
    arrow(ax, P(-3, 0), P(3, 0), 'sujet', lw=1.2)
    arrow(ax, P(0, -3), P(0, 3), 'autre', lw=1.2)
    text(ax, P(3, 0)[0] - 1, P(3, 0)[1] - 3.5, 'X', 'sujet', 's', weight='bold')
    text(ax, P(0, 3)[0] + 3.5, P(0, 3)[1], 'Y', 'autre', 's', weight='bold')
    if three:
        arrow(ax, P(-2.8, -2.8), P(2.8, 2.8), 'varie', lw=1.2)
        text(ax, P(2.8, 2.8)[0] - 3, P(2.8, 2.8)[1] + 2.5, 'Z', 'varie', 's', weight='bold')
    disc(ax, ox, oy, 1.3, 'resultat' if not three else 'limite')
plane(22, False)
plane(66, True)
text(ax, 22, 60, 'indépendants', 'resultat', 'm', weight='bold')
text(ax, 66, 60, 'pas indépendants', 'limite', 'm', weight='bold')
text(ax, 22, 7, r'$X\cap Y=\{O\}$', 'resultat', 's', weight='bold')
text(ax, 66, 7, r'$Z\cap(X+Y)\neq\{O\}$', 'limite', 's', weight='bold')
save(fig, '58-252')
