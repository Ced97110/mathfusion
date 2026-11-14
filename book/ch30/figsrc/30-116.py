import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(80)
cx, cy, r = 22, 42, 18
disc(ax, cx, cy, r, 'sujet', fill=False, lw=1.0)
line(ax, [(50, cy - r), (50, cy + r)], 'fixe')
text(ax, 50, cy + r + 3.5, '1', 'fixe', 's'); text(ax, 50, cy - r - 3.5, r'$-1$', 'fixe', 's')
for ang, lab in ((math.pi / 4, r'$\pi/4 \to 0{,}707$'), (math.pi / 2, r'$\pi/2 \to 1$'),
                 (3 * math.pi / 2, r'$3\pi/2 \to -1$'), (100 % (2 * math.pi), r'$100 \to -0{,}506$')):
    px, py = cx + r * math.cos(ang), cy + r * math.sin(ang)
    line(ax, [(px, py), (50, py)], 'varie', lw=0.6, dash=True)
    disc(ax, px, py, 1.2, 'varie'); disc(ax, 50, py, 1.2, 'resultat')
    text(ax, 54, py, lab, 'resultat', 's', ha='left')
text(ax, 44, 12, 'la hauteur reste entre −1 et 1', 'encre', 's')
save(fig, '30-116')
