import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
R = 17
def pts(cx, cy):
    return [(cx + R * math.cos(math.pi / 2 + 2 * math.pi * k / 16), cy + R * math.sin(math.pi / 2 + 2 * math.pi * k / 16)) for k in range(16)]
L, Rr = pts(22, 30), pts(66, 30)
for a in range(16):
    for b in range(a + 1, 16):
        line(ax, [L[a], L[b]], 'fixe', lw=0.3)
for b in range(1, 16):
    line(ax, [Rr[0], Rr[b]], 'sujet', lw=0.6)
for p in L: disc(ax, p[0], p[1], 1.2, 'fixe')
for k, p in enumerate(Rr): disc(ax, p[0], p[1], 1.2 if k else 2.0, 'sujet' if k else 'resultat')
text(ax, 22, 58, '120 distances', 'fixe', 'm')
text(ax, 66, 58, '15 poids', 'sujet', 'm')
text(ax, 66, 52, 'mot nul', 'resultat', 's')
text(ax, 44, 5, 'code linéaire de 16 mots', 'encre', 'm')
save(fig, '68-106')
