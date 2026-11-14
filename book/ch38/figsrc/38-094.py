import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(66)
# échelle : 1 m = 0,18 mm. AP = 269,5 m ; AQ = 347,4 m ; angle PAQ = 30°
k = 0.18
A = (6.0, 14.0)
Q = (A[0] + 347.4 * k, A[1])
a = math.radians(30)
P = (A[0] + 269.5 * k * math.cos(a), A[1] + 269.5 * k * math.sin(a))
H = (P[0], A[1])                     # pied de la perpendiculaire de P sur AQ : AH = AP cos 30°
poly(ax, [A, Q, P], 'fixe')
arrow(ax, A, Q, 'autre', lw=1.5)
arrow(ax, A, P, 'sujet', lw=1.5)
line(ax, [P, H], 'fixe', dash=True)
# projection de AP sur AQ, décalée sous la base pour rester visible
ax.plot([A[0], H[0]], [A[1] - 2.4, H[1] - 2.4], color=COL['varie'], lw=3.0, zorder=6, solid_capstyle='butt')
line(ax, [P, Q], 'resultat', lw=1.6)
arc(ax, A[0], A[1], 9, 0, 30, 'varie')
text(ax, 18.5, A[1] + 1.8, r'$30°$', 'varie', 's', ha='left')
text(ax, 21, A[1] + 15.5, r'$AP=269{,}5$ m', 'sujet', 's', ha='right')
text(ax, 62, A[1] - 3.5, r'$AQ=347{,}4$ m', 'autre', 's')
text(ax, 61, A[1] + 17, r'$PQ\approx176{,}5$ m', 'resultat', 's', ha='left')
text(ax, 28, A[1] - 7, r'$AP\cos30°$', 'varie', 's')
# la formule : le terme du milieu est mis dans une case orange
text(ax, 4, 56, r'$PQ^2=AP^2+AQ^2-2$', 'encre', 's', ha='left')
box(ax, 44, 51, 40, 10, 'varie', label=r'$AP\cdot AQ\cos30°$', size='s')
arrow(ax, (64, 51), (64, 44), 'varie', lw=1.2)
text(ax, 64, 41, 'produit scalaire de AP et AQ', 'varie', 's', weight='bold')
save(fig, '38-094')
