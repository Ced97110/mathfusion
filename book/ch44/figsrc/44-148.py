import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 28, 33, 24
P = lambda k, rad: (cx + rad * math.sin(math.radians(45 * k)), cy + rad * math.cos(math.radians(45 * k)))
for k in range(8):
    disc(ax, *P(k, R), 4.2, 'resultat' if k == 7 else 'fixe', label=str(k), size='s')
pts = [P(t / 4, 17 - 0.45 * t / 4) for t in range(0, 61)]
line(ax, pts[:33], 'fixe', lw=1.2)
line(ax, pts[32:57], 'resultat', lw=1.2)
arrow(ax, pts[56], pts[60], 'resultat', lw=1.2)
text(ax, 58, 50, '3 × 5 = 15 pas', 'sujet', 'm', ha='left')
text(ax, 58, 40, '1 tour : 8 pas', 'fixe', 'm', ha='left')
text(ax, 58, 32, 'puis 7 pas', 'resultat', 'm', ha='left')
text(ax, 58, 22, '15 = 8 + 7', 'encre', 'm', ha='left')
text(ax, 58, 14, 'arrivée sur 7', 'resultat', 'm', ha='left')
save(fig, '44-148')
