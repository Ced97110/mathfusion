import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(cx, cy, r, d):
    return (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
def arc(ax, cx, cy, r, a0, a1, role, lw=0.9, dash=False, n=90):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def circ_axes(ax, cx, cy, r, ext=3):
    line(ax, [(cx - r - ext, cy), (cx + r + ext, cy)], "fixe", 0.5)
    line(ax, [(cx, cy - r - ext), (cx, cy + r + ext)], "fixe", 0.5)
    arc(ax, cx, cy, r, 0, 360, "fixe", 0.8)
def pt(ax, cx, cy, r, d, role, rr=1.3):
    x, y = P(cx, cy, r, d); disc(ax, x, y, rr, role)

fig, ax = canvas(62)
cy, r = 33, 11
cols = [(15, 'sin', 30, 150, '30° → 150°', '180° − α'),
        (44, 'cos', 60, -60, '60° → −60°', '−α'),
        (73, 'tan', 45, 225, '45° → 225°', 'α + 180°')]
for cx, nm, a, b, nums, form in cols:
    circ_axes(ax, cx, cy, r, 2.5)
    pa, pb = P(cx, cy, r, a), P(cx, cy, r, b)
    line(ax, [pa, pb], 'fixe', 0.8, True)
    disc(ax, pa[0], pa[1], 1.3, 'sujet'); disc(ax, pb[0], pb[1], 1.3, 'resultat')
    text(ax, cx, cy + r + 6.5, nm, 'encre', 'l', weight='bold')
    text(ax, cx, cy - r - 6, nums, 'fixe', 's')
    text(ax, cx, cy - r - 11, form, 'resultat', 's')
text(ax, 44, 57, 'même rôle : angle partenaire', 'resultat', 'm')
save(fig, '32-083')
