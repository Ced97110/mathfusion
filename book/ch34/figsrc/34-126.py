import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
L = 30
text(ax, 44, 62, r'$QH=p\ \cos(\alpha+\beta)$, $p=15$', 'encre', 'm')
def panel(qx, th, role, cap):
    Q = (qx, 50)
    S = (qx + L * math.sin(math.radians(th)), 50 - L * math.cos(math.radians(th)))
    H = (qx, S[1])
    line(ax, [(qx, 52), (qx, 14)], 'fixe', lw=0.7, dash=True)
    line(ax, [Q, S], role, lw=1.2)
    disc(ax, *Q, 1.3, 'sujet'); disc(ax, *S, 1.3, role)
    return Q, S, H
Q1, S1, H1 = panel(8, 50, 'autre', '')
line(ax, [Q1, H1], 'resultat', lw=2.2); line(ax, [H1, S1], 'fixe', lw=0.9)
line(ax, [(H1[0], H1[1] + 3), (H1[0] + 3, H1[1] + 3), (H1[0] + 3, H1[1])], 'fixe', lw=0.7)
text(ax, Q1[0] - 2.5, Q1[1], 'Q', 'sujet', 'm', ha='right'); text(ax, H1[0] - 2.5, H1[1], 'H', 'resultat', 'm', ha='right')
text(ax, S1[0] + 2.5, S1[1], 'S', 'autre', 'm', ha='left')
text(ax, 34, 42, '15', 'autre', 's')
text(ax, 20, 8, r'$\cos>0$ : QH > 0', 'resultat', 's')
Q2, S2, H2 = panel(54, 90, 'autre', '')
line(ax, [(Q2[0], Q2[1] - 3), (Q2[0] + 3, Q2[1] - 3), (Q2[0] + 3, Q2[1])], 'fixe', lw=0.7)
text(ax, Q2[0] - 2.5, Q2[1] + 3, 'Q = H', 'resultat', 'm', ha='right')
text(ax, S2[0] + 1, S2[1] + 3.5, 'S', 'autre', 'm', ha='right')
text(ax, 69, 53.5, '15', 'autre', 's')
text(ax, 66, 8, r'$\cos=0$ : QH = 0', 'resultat', 's')
text(ax, 66, 30, 'angle droit en Q', 'fixe', 's')
save(fig, '34-126')
