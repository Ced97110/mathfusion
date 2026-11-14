import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(86)
def pt(cx, cy, R, th):
    t = math.radians(th)
    return (cx + R * math.sin(t), cy + R * math.cos(t))
cx, cy, R = 28, 43, 19
for k in range(10):
    role = 'varie' if k == 7 else ('resultat' if k == 2 else 'sujet')
    disc(ax, *pt(cx, cy, R, 36 * k), 3.8, role, label=str(k), size='s')
text(ax, cx, cy, 'ℤ/10', 'sujet', 'm', weight='bold')
# 7 + 5 = 12, soit 2 : arc de 5 pas, de l'heure 7 à l'heure 2
Ra = R + 6.5
arc = [pt(cx, cy, Ra, 252 + 180 * i / 60) for i in range(61)]
line(ax, arc[:-3], 'varie', lw=1.3)
arrow(ax, arc[-4], arc[-1], 'varie', lw=1.3)
# horloge à 2 heures
c2x, c2y = 72, 43
for k in range(2):
    disc(ax, *pt(c2x, c2y, 8, 180 * k), 3.8, 'autre', label=str(k), size='s')
text(ax, c2x, c2y, 'ℤ/2', 'autre', 'm', weight='bold')
save(fig, '59-121')
