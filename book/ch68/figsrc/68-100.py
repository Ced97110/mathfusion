import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
cx, cy, R = 24, 28, 20
P = [(cx + R * math.cos(2 * math.pi * k / 16), cy + R * math.sin(2 * math.pi * k / 16)) for k in range(16)]
for a in range(16):
    for b in range(a + 1, 16):
        line(ax, [P[a], P[b]], 'fixe', lw=0.3)
for p in P:
    disc(ax, p[0], p[1], 1.3, 'sujet')
text(ax, 24, 53, '16 mots : 120 paires', 'sujet', 'm')
text(ax, 67, 36, r'$2^{24}$ mots :', 'autre', 'm')
text(ax, 67, 28, r'$\approx 1{,}4 \times 10^{14}$', 'autre', 'm')
text(ax, 67, 21, 'paires', 'autre', 'm')
save(fig, '68-100')
