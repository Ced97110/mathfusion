import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4))
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw)
    arrow(ax, pts[-2], pts[-1], role, lw)
def sq(ax, cx, cy, h, role, fill=True, dash=False, rot=0):
    pts = [(cx + h * math.sqrt(2) * math.cos(math.radians(45 + 90 * k + rot)), cy + h * math.sqrt(2) * math.sin(math.radians(45 + 90 * k + rot))) for k in range(4)]
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role] if fill else "none", lw=0.9, ls="--" if dash else "-", zorder=2))

fig, ax = canvas(64)
text(ax, 44, 59, r'$\mathrm{Sym}(X)$ : les isométries avec $f(X)=X$', 'encre', 's')
cy = 34; h = 6
# 1 quart de tour
cx = 16
sq(ax, cx, cy, h, 'sujet')
disc(ax, cx + h, cy + h, 1.1, 'fixe'); disc(ax, cx - h, cy + h, 1.1, 'varie')
arc(ax, cx, cy, 11, 45, 130, 'varie', 1.0)
text(ax, cx, 17, 'quart de tour', 'resultat', 's'); text(ax, cx, 12, r'$f(X)=X$', 'resultat', 's')
# 2 glissement
cx = 44
sq(ax, cx - 7, cy, h, 'sujet'); sq(ax, cx + 7, cy, h, 'varie', fill=False, dash=True)
arrow(ax, (cx - 7, cy - 9), (cx + 7, cy - 9), 'varie')
text(ax, cx, 17, 'glissement de 1', 'limite', 's'); text(ax, cx, 12, r'$f(X)\neq X$', 'limite', 's')
# 3 identité
cx = 72
sq(ax, cx, cy, h, 'sujet')
for k in range(4):
    disc(ax, cx + h * math.sqrt(2) * math.cos(math.radians(45 + 90 * k)), cy + h * math.sqrt(2) * math.sin(math.radians(45 + 90 * k)), 1.1, 'fixe')
text(ax, cx, 17, 'identité', 'resultat', 's'); text(ax, cx, 12, r'$f(X)=X$', 'resultat', 's')
save(fig, '74-057')
