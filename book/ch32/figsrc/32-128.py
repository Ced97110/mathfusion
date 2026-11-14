import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, r = 44, 44, 20
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(cx - r - 2, cy), (cx + r + 2, cy)], 'sujet', lw=1.4)
pts = []
for i in range(0, 541, 5):
    a = math.radians(i); rr = r * (1.12 + 0.3 * i / 540)
    pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
line(ax, pts, 'limite', lw=1.0)
arrow(ax, pts[-3], pts[-1], 'limite')
disc(ax, cx + r, cy, 1.9, 'resultat'); disc(ax, cx - r, cy, 1.9, 'resultat')
text(ax, cx + r - 6, cy + 4, '0°', 'resultat', 's')
text(ax, cx - r + 6, cy + 4, '180°', 'resultat', 's')
text(ax, 8, cy, '540°', 'limite', 's')
text(ax, 44, 14, 'OP horizontale : tan x = 0', 'sujet', 's')
text(ax, 44, 7, '540° aussi : tan 540° = 0', 'limite', 's')
save(fig, '32-128')
