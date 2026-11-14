import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def panel(cx, n, R, title, sub):
    cy = 36
    pts = [(cx + R * math.cos(math.radians(360 * k / n)), cy + R * math.sin(math.radians(360 * k / n))) for k in range(n)]
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=2))
    poly(ax, pts, 'sujet')
    for p in pts: disc(ax, p[0], p[1], 1.5, 'sujet')
    text(ax, cx, 14, title, 'sujet', 's', weight='bold'); text(ax, cx, 9.5, sub, 'sujet', 's')
panel(23, 3, 18, '3 racines', 'triangle équilatéral')
panel(65, 6, 18, '6 racines', 'hexagone régulier')
text(ax, 44, 65, 'n racines : n sommets, mêmes côtés', 'encre', 's')
text(ax, 23, 59, 'cube de chaque sommet = 8', 'fixe', 's')
text(ax, 65, 59, 'puissance 6 = 1', 'fixe', 's')
save(fig, '39-095')
