import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
def plane(x0, role, n):
    box(ax, x0, 6, 30, 38, 'fixe', fill=False, dash=True)
    ox, oy, s = x0 + 6, 12, 15
    poly(ax, [(ox, oy), (ox + s, oy), (ox + s, oy + s), (ox, oy + s)], role)
    text(ax, ox + s / 2, oy + s / 2, '1', role, 'l')
    arrow(ax, (ox, oy), (ox + s + 6, oy), 'sujet', lw=1.2); arrow(ax, (ox, oy), (ox, oy + s + 6), 'sujet', lw=1.2)
    text(ax, ox + s + 6, oy - 3, rf'$e_{n}$', 'sujet'); text(ax, ox - 3, oy + s + 6, rf'$f_{n}$', 'sujet')
    text(ax, x0 + 15, 47, rf'$P_{n}$', 'sujet', 'l')
plane(4, 'resultat', 1); plane(54, 'resultat', 2)
text(ax, 44, 30, r'$\perp$', 'limite', 'xl', weight='bold')
text(ax, 44, 20, 'aires nulles', 'limite', 's')
arrow(ax, (36, 25), (52, 25), 'limite', both=True)
save(fig, '75-033')
