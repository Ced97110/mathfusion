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

fig, ax = canvas(50)
tx = lambda a: 10 + 0.2 * a
yy = lambda v: 30 + 10 * v
th = list(range(0, 361))
line(ax, [(8, 30), (84, 30)], 'fixe', 0.5)
line(ax, [(tx(a), yy(math.sin(math.radians(a)))) for a in th], 'fixe', 1.0, True)
line(ax, [(tx(a), yy(math.sin(math.radians(2 * a)))) for a in th], 'sujet', 1.4)
line(ax, [(8, yy(0.5)), (84, yy(0.5))], 'varie', 1.0)
for a in (15, 75, 195, 255):
    line(ax, [(tx(a), yy(0.5)), (tx(a), 16.5)], 'fixe', 0.5, True)
    disc(ax, tx(a), yy(0.5), 1.3, 'resultat')
    text(ax, tx(a), 13.5, f'{a}°', 'resultat', 's')
text(ax, tx(225), 43.5, 'sin 2θ', 'sujet', 's')
text(ax, tx(90), 43.5, 'sin θ', 'fixe', 's')
text(ax, 78, 37.5, 'y = 0,5', 'varie', 's')
text(ax, 44, 6, '4 croisements : 4 angles', 'resultat', 'm')
save(fig, '32-094')
