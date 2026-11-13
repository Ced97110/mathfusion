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

fig, ax = canvas(74)
f = numberline(ax, 8, 80, 50, -180, 360, step=180, arrow_right=False)
box(ax, f(-180), 45, f(180) - f(-180), 10, 'sujet')
text(ax, f(0), 53.3, 'intervalle', 'sujet', 's')
disc(ax, f(191.54), 50, 1.4, 'varie'); disc(ax, f(-168.46), 50, 1.4, 'resultat')
arrow(ax, (f(191.54), 52), (f(-168.46), 52), 'varie', curve=0.25)
text(ax, f(12), 66, '− 360°', 'varie', 'm')
text(ax, f(191.54), 41, '191,54°', 'varie', 's')
text(ax, f(-168.46), 41, '−168,46°', 'resultat', 's')
cx, cy, r = 38, 17, 10
circ_axes(ax, cx, cy, r, 2.5)
arc(ax, cx, cy, 5.5, 0, 191.54, 'varie', 1.0)
arc(ax, cx, cy, 7.5, 0, -168.46, 'resultat', 1.0)
pt(ax, cx, cy, r, 191.54, 'resultat', 1.5)
text(ax, cx - r - 4, cy + 3.5, '191,54°', 'varie', 's', ha='right')
text(ax, cx - r - 4, cy - 3.5, '−168,46°', 'resultat', 's', ha='right')
text(ax, 68, cy, 'même point', 'resultat', 'm')
save(fig, '32-091')
