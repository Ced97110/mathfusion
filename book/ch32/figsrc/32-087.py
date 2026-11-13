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

fig, ax = canvas(56)
top, bot, h = 36, 10, 10
spec = [(11, 16, '30t', 't', 'sujet', 'sujet'), (34, 14, '30°', '1', 'fixe', 'resultat'), (55, 22, '360°n', '12n', 'fixe', 'resultat')]
for x, w, a, b, ra, rb in spec:
    box(ax, x, top, w, h, ra, label=a, size='l')
    box(ax, x, bot, w, h, rb, label=b, size='l')
    arrow(ax, (x + w / 2, top), (x + w / 2, bot + h), 'varie')
    text(ax, x + w / 2 + 2.5, (top + bot + h) / 2, '÷ 30', 'varie', 's', ha='left')
for yy in (top, bot):
    text(ax, 30.5, yy + h / 2, '=', 'encre', 'l'); text(ax, 51.5, yy + h / 2, '+', 'encre', 'l')
text(ax, 66, 4.5, '12 h = la période', 'resultat', 'm')
save(fig, '32-087')
