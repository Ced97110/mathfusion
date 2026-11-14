import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
cx, cy, U = 46, 40, 18.0          # 1 unité = 18 mm
R = 2 ** (1 / 3)                  # racine cubique réelle de 2 (≈ 1,26)
arrow(ax, (3, cy), (82, cy), 'fixe', lw=0.8)
arrow(ax, (cx, 8), (cx, 72), 'fixe', lw=0.8)
# le corps réel : tout l'axe réel
line(ax, [(5, cy), (80, cy)], 'sujet', lw=2.4)
text(ax, 20, cy - 4.5, 'corps réel', 'sujet', 's')
pts = [(R * math.cos(a), R * math.sin(a)) for a in (0, 2 * math.pi / 3, 4 * math.pi / 3)]
# racine réelle dans le corps
disc(ax, cx + pts[0][0] * U, cy, 1.7, 'sujet')
text(ax, cx + pts[0][0] * U + 1, cy + 5.5, r'$1{,}26$', 'sujet', 's')
text(ax, cx + pts[0][0] * U + 1, cy + 9.5, 'dans le corps', 'sujet', 's', ha='center')
# les deux autres racines : hors du corps
for (a, b), lab in zip(pts[1:], (r'$1{,}26\ w$', r'$1{,}26\ w^2$')):
    X, Y = cx + a * U, cy + b * U
    disc(ax, X, Y, 1.7, 'varie')
    text(ax, X - 3, Y, lab, 'varie', 's', ha='right')
text(ax, 20, 71, 'hors du corps réel', 'varie', 's')
text(ax, 44, 4, r'$x^3-2=0$ : il manque $w$', 'encre', 's')
save(fig, '65-127')
