import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy, r = 44, 44, 26
fig, ax = canvas(90)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
n = 6
pts = [(cx + r * math.cos(math.radians(60 * k)), cy + r * math.sin(math.radians(60 * k))) for k in range(n)]
# flèches le long du cercle : arc de k*60° à (k+1)*60°, raccourci de 4° à chaque bout
for k in range(n):
    a0, a1 = 60 * k + 5, 60 * (k + 1) - 5
    ro = r + 5
    ax.add_patch(Arc((cx, cy), 2 * ro, 2 * ro, theta1=a0, theta2=a1, ec=COL['resultat' if k == n - 1 else 'varie'], lw=1.2, zorder=3))
    ex, ey = cx + ro * math.cos(math.radians(a1)), cy + ro * math.sin(math.radians(a1))
    tx, ty = -math.sin(math.radians(a1)), math.cos(math.radians(a1))
    arrow(ax, (ex - tx * 0.8, ey - ty * 0.8), (ex + tx * 0.5, ey + ty * 0.5), 'resultat' if k == n - 1 else 'varie', lw=1.2)
for k in range(n):
    disc(ax, pts[k][0], pts[k][1], 1.5, 'sujet')
labs = ['1', r'$\omega$', r'$\omega^2$', r'$\omega^3$', r'$\omega^4$', r'$\omega^5$']
offs = [(-5, 0, 'right'), (-1, -4.5, 'center'), (1, -4.5, 'center'), (5, 0, 'left'), (1, 4.5, 'center'), (-1, 4.5, 'center')]
# étiquettes à l'intérieur du cercle
inn = 5.5
for k in range(n):
    a = math.radians(60 * k)
    text(ax, cx + (r - inn) * math.cos(a), cy + (r - inn) * math.sin(a), labs[k], 'sujet', 'm')
text(ax, cx, cy + 4, '6 éléments', 'sujet', 'm')
text(ax, cx, cy - 4, r'$\omega^6=1$', 'resultat', 'm')
text(ax, 4, 85, r'$\omega=\mathrm{cis}\,60°$', 'encre', 's', ha='left')
text(ax, 84, 85, r'$\times\,\omega$ à chaque pas', 'varie', 's', ha='right')
save(fig, '39-104')
