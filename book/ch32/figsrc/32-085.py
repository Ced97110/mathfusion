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

fig, ax = canvas(46)
x0, x1, y = 6, 78, 20
box(ax, x0, y - 6, x1 - x0, 12, 'sujet')
f = numberline(ax, x0, x1, y, 0, 720, step=360, arrow_right=False)
for v in (30, 150, 390, 510):
    disc(ax, f(v), y, 1.4, 'resultat')
    text(ax, f(v), y + 9, f'{v}°', 'resultat', 's')
disc(ax, f(750), y, 1.4, 'limite')
text(ax, f(750), y + 9, '750°', 'limite', 's')
text(ax, 82, 9, 'écarté', 'limite', 's')
text(ax, 32, 8, '4 angles gardés', 'resultat', 'm')
text(ax, 42, 40, 'angle 30t : intervalle de 0° à 720°', 'sujet', 'm')
save(fig, '32-085')
