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
x0, s = 12, 0.09
fx = lambda v: x0 + v * s
line(ax, [(x0, 40), (fx(720), 40)], 'sujet', 1.0)
line(ax, [(x0, 19), (x0 + 360 * 2 * s, 19)], 'resultat', 1.0)
text(ax, x0 - 2, 40, '0°', 'sujet', 's', ha='right'); text(ax, fx(720) + 2, 40, '720°', 'sujet', 's', ha='left')
text(ax, x0 - 2, 19, '0°', 'resultat', 's', ha='right'); text(ax, fx(720) + 2, 19, '360°', 'resultat', 's', ha='left')
for y_ in (30, 150, 390, 510):
    disc(ax, fx(y_), 40, 1.4, 'sujet'); text(ax, fx(y_), 44.5, f'{y_}°', 'sujet', 's')
    disc(ax, fx(y_), 19, 1.4, 'resultat'); text(ax, fx(y_), 14.5, f'{y_ // 2}°', 'resultat', 's')
    arrow(ax, (fx(y_), 38), (fx(y_), 21), 'varie')
text(ax, 72, 29.5, '÷ 2', 'varie', 'm')
text(ax, 44, 52, 'y = 2θ, sin y = 0,5, y jusqu’à 720°', 'sujet', 's')
save(fig, '32-095')
