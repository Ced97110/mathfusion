import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
c30 = math.cos(math.radians(30))
text(ax, 13, 54, 'nom court', 'encre', 's'); text(ax, 47, 54, 'contenu', 'encre', 's'); text(ax, 77, 54, 'axe', 'encre', 's')
for i, k in enumerate('ABC'):
    y = 40 - 14 * i
    box(ax, 4, y - 4.5, 18, 9, 'sujet', label=r'$P_%s$' % k, size='m')
    arrow(ax, (23, y), (30, y), 'fixe')
    box(ax, 31, y - 4.5, 34, 9, 'fixe', label=r'$\{e,\ s_%s\}$' % k, size='m')
    cx, cy, R = 77, y, 4.6
    V = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
    poly(ax, list(V.values()), 'fixe')
    v = V[k]; d = ((cx - v[0]) / R, (cy - v[1]) / R)
    line(ax, [(v[0] - d[0], v[1] - d[1]), (v[0] + d[0] * (1.5 * R + 1), v[1] + d[1] * (1.5 * R + 1))], 'varie', lw=1.0, dash=True)
text(ax, 44, 5, r'$A, B, C$ : l’axe de la réflexion', 'encre', 's')
save(fig, '50-086')
