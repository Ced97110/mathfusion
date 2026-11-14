import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 6.0
def panel(ox, oy, a, b, ra, rb):
    P = lambda x, y: (ox + s * x, oy + s * y)
    line(ax, [P(0, 0), P(3.2, 0)], 'fixe', lw=0.4); line(ax, [P(0, 0), P(0, 4.6)], 'fixe', lw=0.4)
    arrow(ax, P(0, 0), P(*a), ra, lw=1.5)
    arrow(ax, P(0, 0), P(*b), rb, lw=1.5)
    return P
# gauche : colinéaires
Pl = panel(6, 22, (2, 4), (1, 2), 'sujet', 'autre')
text(ax, Pl(2, 4)[0] + 6, Pl(2, 4)[1], '(2, 4)', 'sujet', 's')
text(ax, Pl(1, 2)[0] + 7, Pl(1, 2)[1] - 1, '(1, 2)', 'autre', 's')
text(ax, 22, 62, 'sur la même droite', 'resultat', 's')
text(ax, 22, 12, r'$1\times(2,4)-2\times(1,2)=0$', 'resultat', 's')
text(ax, 22, 5, 'liés', 'resultat', 'm', weight='bold')
# droite : non colinéaires
Pr = panel(50, 22, (1, 2), (2, 1), 'autre', 'sujet')
text(ax, Pr(1, 2)[0] + 1, Pr(1, 2)[1] + 4, '(1, 2)', 'autre', 's')
text(ax, Pr(2, 1)[0] + 6, Pr(2, 1)[1] - 1, '(2, 1)', 'sujet', 's')
text(ax, 66, 62, 'deux droites', 'fixe', 's')
text(ax, 66, 12, 'aucun multiple de l’autre', 'fixe', 's')
text(ax, 66, 5, 'pas liés', 'fixe', 'm', weight='bold')
line(ax, [(44, 3), (44, 66)], 'fixe', lw=0.4, dash=True)
save(fig, '58-161')
