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

fig, ax = canvas(70)
cx, cy, r = 44, 40, 22
circ_axes(ax, cx, cy, r)
arc(ax, cx, cy, 12, 0, -11.54, 'sujet', 1.4)
arc(ax, cx, cy, 15, 0, 191.54, 'varie', 1.0, True)
pt(ax, cx, cy, r, -11.54, 'sujet', 1.5)
pt(ax, cx, cy, r, 191.54, 'resultat', 1.5)
text(ax, cx + r + 4, cy - 4.4, '−11,54°', 'sujet', 'm', ha='left')
text(ax, cx - r + 1, cy + 4, '191,54°', 'varie', 'm', ha='right')
text(ax, cx - r + 1, cy - 9, '= −168,46°', 'resultat', 'm', ha='right')
text(ax, 44, 8, '191,54° − 360° = −168,46°', 'fixe', 's')
save(fig, '32-089')
