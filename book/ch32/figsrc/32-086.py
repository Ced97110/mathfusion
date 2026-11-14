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

fig, ax = canvas(58)
f = numberline(ax, 6, 78, 22, 0, 24, step=1, arrow_right=False, every=12)
for t in (1, 5, 13, 17):
    role = 'sujet' if t in (1, 13) else 'autre'
    disc(ax, f(t), 22, 1.5, role)
    text(ax, f(t), 28.5, str(t), role, 'm')
brace(ax, f(0) + 0.5, f(12) - 0.5, 35, 'fixe', '1 tour : 2 solutions', down=False)
brace(ax, f(12) + 0.5, f(24) - 0.5, 35, 'fixe', '1 tour : 2 solutions', down=False)
text(ax, 44, 52, 'sin(30t) = 0,5 sur 24 h', 'encre', 'm')
text(ax, 24, 8, '30° + 360°n → t = 1 + 12n', 'sujet', 's')
text(ax, 64, 8, '150° + 360°n → t = 5 + 12n', 'autre', 's')
save(fig, '32-086')
