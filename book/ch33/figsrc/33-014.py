import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 70 / 540; xo = 8 + 180 * k
X = lambda d: xo + d * k
rows = [(44, 'tous les angles', 'fixe', -180, 360), (30, 'un tour : 0° à 360°', 'autre', 0, 360), (16, 'bande : −90° à 90°', 'sujet', -90, 90)]
for y, lab, r, a, b in rows:
    ax.add_patch(Rectangle((X(a), y), (b - a) * k, 6, fc=FILL[r], ec=COL[r], lw=0.8, zorder=2))
    text(ax, X(a) + 1.5, y + 9.5, lab, r, 's', ha='left')
for d in (-90, 90):
    line(ax, [(X(d), 12), (X(d), 23)], 'sujet', lw=0.6, dash=True)
text(ax, X(-90), 6, r'$-\pi/2$', 'sujet', 's')
text(ax, X(90), 6, r'$\pi/2$', 'sujet', 's')
brace(ax, X(-90), X(90), 14, 'sujet', label=None)
text(ax, X(0), 6, 'largeur π', 'sujet', 's')
save(fig, '33-014')
