import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
cx, cy, R, rd = 21, 46, 16, 2.4
pos = lambda h, rr=R: (cx + rr * math.sin(math.radians(30 * h)), cy + rr * math.cos(math.radians(30 * h)))
for h in range(6):
    a, b = pos(h, R - rd), pos(h + 6, R - rd)
    line(ax, [a, b], 'varie' if h in (0, 3) else 'fixe', lw=1.5 if h in (0, 3) else 0.7)
for h in range(12):
    x, y = pos(h)
    disc(ax, x, y, rd, 'resultat' if h in (0, 3, 6, 9) else 'fixe', label=str(h) if h % 3 == 0 else None, size='s')
text(ax, cx, 69, '$G$', 'fixe', 's')
box(ax, 54, 36, 32, 34, 'sujet', fill=False)
text(ax, 70, 65, r'$G/\langle 6\rangle$', 'sujet', 's')
for k in range(6):
    r_, c_ = divmod(k, 3); x = 56.5 + c_ * 10; y = 52 - r_ * 11
    on = k in (0, 3)
    box(ax, x, y, 7.5, 7, 'varie' if on else 'fixe', r=0.4, label=['{0,6}', '{3,9}'][[0, 3].index(k)] if on else None, size='s')
arrow(ax, (41, 60), (53, 60), 'sujet'); text(ax, 47, 63, '1', 'sujet', 's', weight='bold')
text(ax, 59, 38.5, '2', 'varie', 's', weight='bold')
arrow(ax, (53, 42), (41, 42), 'resultat'); text(ax, 47, 38.5, '3', 'resultat', 's', weight='bold')
text(ax, 3, 22, r'1. quotient par $\langle 6\rangle$ : 6 paquets', 'sujet', 's', ha='left')
text(ax, 3, 14, '2. sous-groupe de 2 paquets', 'varie', 's', ha='left')
text(ax, 3, 6, '3. on remonte : 0, 3, 6, 9', 'resultat', 's', ha='left')
save(fig, '50-127')
