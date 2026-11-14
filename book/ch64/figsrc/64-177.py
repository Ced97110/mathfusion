import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
yz, k = 22, 0.6
ya, yb = yz - 3 * k, yz + 67 * k
text(ax, 22, 69, 'courbe sans saut', 'sujet', 'm', weight='bold')
text(ax, 66, 69, 'avec un saut', 'limite', 'm', weight='bold')
line(ax, [(2, yz), (86, yz)], 'fixe', lw=0.5, dash=True)
# courbe continue : de -3 à 67
pts = []
for i in range(61):
    t = i / 60
    s = t * t * (3 - 2 * t)
    pts.append((6 + 34 * t, ya + (yb - ya) * s))
line(ax, pts, 'sujet', lw=1.2)
disc(ax, 6, ya, 1.3, 'sujet'); disc(ax, 40, yb, 1.3, 'sujet')
text(ax, 10, ya - 4, '−3', 'sujet', 's'); text(ax, 36, yb + 3, '67', 'sujet', 's')
zx = min(p[0] for p in pts if p[1] >= yz)
disc(ax, zx, yz, 1.5, 'resultat')
text(ax, 31, 12, 'passe par zéro', 'resultat', 's')
arrow(ax, (27, 15), (zx + 0.8, yz - 2), 'resultat')
# saut
line(ax, [(50, ya), (66, ya)], 'sujet', lw=1.2); line(ax, [(66, yb), (84, yb)], 'sujet', lw=1.2)
line(ax, [(66, ya), (66, yb)], 'limite', dash=True)
disc(ax, 50, ya, 1.3, 'sujet'); disc(ax, 84, yb, 1.3, 'sujet')
text(ax, 54, ya - 4, '−3', 'sujet', 's'); text(ax, 80, yb + 3, '67', 'sujet', 's')
text(ax, 72, 45, 'pas de zéro', 'limite', 's', ha='left')
save(fig, '64-177')
