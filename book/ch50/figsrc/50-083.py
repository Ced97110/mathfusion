import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 25, 38, 21
c30 = math.cos(math.radians(30))
P = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
poly(ax, list(P.values()), 'fixe')
lab = {'A': (cx, cy + R + 3.4), 'B': (cx - R * c30 - 2.5, cy - R / 2 - 3), 'C': (cx + R * c30 + 2.5, cy - R / 2 - 3)}
for k in 'ABC':
    text(ax, *lab[k], k, 'sujet', 'm', weight='bold')
    v = P[k]; d = ((cx - v[0]) / R, (cy - v[1]) / R)
    end = (v[0] + d[0] * (1.5 * R), v[1] + d[1] * (1.5 * R))
    line(ax, [(v[0] - d[0] * 1.5, v[1] - d[1] * 1.5), (end[0] + d[0] * 2, end[1] + d[1] * 2)], 'varie', lw=1.0, dash=True)
    text(ax, end[0] + d[0] * 5.2, end[1] + d[1] * 5.2, r'$s_%s$' % k, 'varie', 's', weight='bold')
text(ax, 64, 54, r'$s$', 'varie', 16, weight='bold')
text(ax, 71.5, 51, r'$A$', 'sujet', 12, weight='bold')
arrow(ax, (64, 48), (62, 42), 'varie'); arrow(ax, (72, 47), (77, 42), 'sujet')
text(ax, 61.5, 38.5, 'réflexion', 'varie', 's')
text(ax, 77.5, 38.5, r'axe par $A$', 'sujet', 's')
text(ax, 71, 28, 'on la lit « s A »', 'encre', 's')
save(fig, '50-083')
