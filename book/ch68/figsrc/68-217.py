import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, 'chaque droite : somme nulle', 'sujet', 'm', weight='bold')
s = 56.0
V1 = (16.0, 14.0); V2 = (V1[0] + s, 14.0); V3 = (V1[0] + s / 2, 14.0 + s * math.sqrt(3) / 2)
mid = lambda a, b: ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
M12, M13, M23 = mid(V1, V2), mid(V1, V3), mid(V2, V3)
Cn = ((V1[0] + V2[0] + V3[0]) / 3, (V1[1] + V2[1] + V3[1]) / 3)
rad = math.hypot(Cn[0] - M12[0], Cn[1] - M12[1])
# les 7 droites : 3 côtés, 3 médianes, 1 cercle (sauf la droite en orange)
for a, b in [(V1, V3), (V2, V3), (V1, M23), (V2, M13), (V3, M12)]:
    line(ax, [a, b], 'fixe', lw=0.9)
ax.add_patch(Circle(Cn, rad, ec=COL['fixe'], fc='none', lw=0.9, zorder=3))
line(ax, [V1, V2], 'varie', lw=1.8)
pts = [(V1, '001', 1), (V2, '010', 1), (M12, '011', 1), (V3, '100', 0), (M13, '101', 0), (M23, '110', 0), (Cn, '111', 0)]
for (px, py), lab, on in pts:
    disc(ax, px, py, 4.6, 'varie' if on else 'sujet', label=lab, size='s')
    ax.patches[-1].set_zorder(3.5)
text(ax, 44, 4.5, r'$001+010+011=000$', 'varie', 's')
save(fig, '68-217')
