import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
x0, y0, L = 4, 26, 76
t = math.radians(6)
B = (x0 + L * math.cos(t), y0); C = (B[0], y0 + L * math.sin(t))
line(ax, [(x0, y0), B], 'fixe', lw=1.2, dash=True)
line(ax, [(x0, y0), C], 'sujet', lw=1.8)
line(ax, [B, C], 'resultat', lw=2.0)
arc = [(x0 + 20 * math.cos(a * t / 20), y0 + 20 * math.sin(a * t / 20)) for a in range(21)]
line(ax, arc, 'varie', lw=1.0)
text(ax, x0 + 27, y0 + 4.5, '6°', 'varie', 'm', ha='left')
text(ax, x0 + 36, y0 + 11, 'route 2 000 m', 'sujet', 'm')
text(ax, B[0] - 2, y0 - 3.5, 'avancée', 'fixe', 's')
text(ax, B[0] - 1, y0 + L * math.sin(t) / 2 + 5.5, 'montée', 'resultat', 's', ha='right') if False else None
box(ax, 6, 5, 76, 12, 'resultat'); text(ax, 44, 11, 'montée = 2 000 × sin 6° ≈ 209 m', 'resultat', 'm', weight='bold')
save(fig, '26-091')
