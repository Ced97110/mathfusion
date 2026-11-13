import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(92)
cx, cy, R = 44.0, 48.0, 24.0
def pt(k, r=R):
    a = math.radians(90 - k * 360 / 26)
    return (cx + r * math.cos(a), cy + r * math.sin(a))
for k in range(26):
    x, y = pt(k)
    role = 'sujet' if k == 0 else ('varie' if k == 3 else 'fixe')
    disc(ax, x, y, 1.6 if role != 'fixe' else 1.1, role)
for k in (0, 3, 25):
    x, y = pt(k, R + 5)
    text(ax, x, y, str(k), 'sujet' if k == 0 else ('varie' if k == 3 else 'fixe'), 'm', weight='bold' if k != 25 else 'normal')
# l'arc de 0 à 3 : trois crans
ri = R - 5
pts = [pt(0 + t / 6 * 3, ri) for t in range(7)]
line(ax, pts[:-1], 'varie', lw=1.4)
arrow(ax, pts[-2], pts[-1], 'varie', lw=1.4)
text(ax, cx, cy + 4, r'$b=3$', 'varie', 'l', weight='bold')
text(ax, cx, cy - 3, '3 crans', 'varie', 's')
text(ax, cx, cy - 9, 'b = 26 : retour à 0', 'fixe', 's')
text(ax, 44, 10, r'$b$ : de 0 à 25, soit 26 valeurs', 'sujet', 'm', weight='bold')
text(ax, 44, 3.5, 'un tour complet = 26 crans', 'fixe', 's')
save(fig, '53-037')
