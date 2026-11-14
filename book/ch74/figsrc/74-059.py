import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4))
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw)
    arrow(ax, pts[-2], pts[-1], role, lw)
def polar(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def sq(ax, cx, cy, h, role):
    pts = [polar(cx, cy, h * math.sqrt(2), 45 + 90 * k) for k in range(4)]
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role], lw=0.9, zorder=2))

fig, ax = canvas(62)
cy = 38
# point
cx = 15
for r in (4, 8):
    ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
disc(ax, cx, cy, 1.6, 'sujet')
text(ax, cx, 21, 'un point', 'encre', 's'); text(ax, cx, 14, r'tout $O(2)$', 'resultat', 'm')
# starfish
cx = 44
pts = [polar(cx, cy, 10 if k % 2 == 0 else 4.2, 90 + 36 * k) for k in range(10)]
ax.add_patch(Polygon(pts, closed=True, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=2))
text(ax, cx, 21, 'étoile à 5 bras', 'encre', 's'); text(ax, cx, 14, '10 symétries', 'varie', 'm')
# F
cx = 72
for sg in [[(0, 0), (0, 14)], [(0, 14), (8, 14)], [(0, 7.5), (6, 7.5)]]:
    line(ax, [(cx - 4 + x, cy - 7 + y) for x, y in sg], 'sujet', lw=2.0)
text(ax, cx, 21, 'la lettre F', 'encre', 's'); text(ax, cx, 14, '1 symétrie', 'limite', 'm')
text(ax, 44, 57, 'même plan, groupes différents', 'encre', 's')
save(fig, '74-059')
