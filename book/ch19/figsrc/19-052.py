import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(76)
for c, s in ((17, r'$0\times x$'), (45, r'$0\times y$')):
    box(ax, c - 9, 61.5, 18, 9, 'fixe', fill=False, dash=True, label=s, size='m')
    line(ax, [(c - 9, 62.5), (c + 9, 69.5)], 'varie', lw=1.2)
text(ax, 31, 66, r'$+$', 'fixe', 'l'); text(ax, 59, 66, r'$=$', 'fixe', 'l')
box(ax, 66.5, 61.5, 9, 9, 'sujet', label=r'$c$', size='l')
text(ax, 70, 55, 'x et y disparaissent', 'varie', 's')
arrow(ax, (44, 60), (44, 49.5), 'varie')
box(ax, 32, 40, 24, 9, 'sujet', label=r'$0=c$', size='l')
arrow(ax, (38, 39), (26, 30), 'fixe'); arrow(ax, (50, 39), (62, 30), 'fixe')
text(ax, 20, 36, r'$c=5$', 'fixe', 's'); text(ax, 68, 36, r'$c=0$', 'fixe', 's')
box(ax, 10, 21, 24, 9, 'limite', label=r'$0=5$', size='l'); box(ax, 54, 21, 24, 9, 'resultat', label=r'$0=0$', size='l')
text(ax, 22, 15, 'faux pour tout couple', 'limite', 's'); text(ax, 66, 15, 'vrai pour tout couple', 'resultat', 's')
save(fig, '19-052')
