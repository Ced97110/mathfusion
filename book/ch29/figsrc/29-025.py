import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
for cx, R, nom, dia, rat in ((22, 9, 'pièce', '2,4 cm', '7,54 ÷ 2,4 ≈ 3,14'), (60, 20, 'roue', '0,7 m', '2,199 ÷ 0,7 ≈ 3,14')):
    cy = 36
    disc(ax, cx, cy, R, 'sujet')
    line(ax, [(cx - R, cy), (cx + R, cy)], 'varie', lw=1.6)
    text(ax, cx, cy + R + 3.5, nom, 'sujet', 'm')
    text(ax, cx, cy - 3.2 if R > 12 else cy + 3.2, dia, 'varie', 's')
    text(ax, cx, 8, rat, 'resultat', 's')
text(ax, 44, 2.5, 'même rapport, tailles différentes', 'fixe', 's') if False else None
save(fig, '29-025')
