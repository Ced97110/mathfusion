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

fig, ax = canvas(60)
tx = lambda t: 10 + 3 * t
yy = lambda h: 12 + 8 * h
ts = [i / 10 for i in range(0, 241)]
hs = [2 + 2 * math.sin(math.radians(30 * t)) for t in ts]
X = [tx(t) for t in ts]; Y = [yy(h) for h in hs]
ax.fill_between(X, [yy(3)] * len(X), Y, where=[y > yy(3) for y in Y], color=FILL['resultat'], lw=0, zorder=1)
line(ax, [(8, yy(3)), (84, yy(3))], 'fixe', 0.8, True)
line(ax, list(zip(X, Y)), 'sujet', 1.3)
numberline(ax, 10, 82, 12, 0, 24, step=1, labels=False, arrow_right=False)
for t in (1, 5, 13, 17):
    disc(ax, tx(t), yy(3), 1.2, 'resultat')
for t in (1, 5, 13, 17, 24):
    text(ax, tx(t), 7.5, str(t), 'fixe', 's')
text(ax, 4.5, yy(3), '3 m', 'fixe', 's'); text(ax, 4.5, yy(4), '4 m', 'fixe', 's')
brace(ax, tx(1), tx(5), 47, 'resultat', '4 h', down=False)
brace(ax, tx(13), tx(17), 47, 'resultat', '4 h', down=False)
text(ax, 44, 57, 'hauteur d’eau sur 24 heures', 'encre', 'm')
save(fig, '32-088')
