import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
R = 9
def tri(cx, cy):   # sommets : haut, bas-droite, bas-gauche (sens horaire)
    return [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, -30, 210)]
def cycle(P, role):
    for i in range(3):
        (x0, y0), (x1, y1) = P[i], P[(i + 1) % 3]
        d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
        arrow(ax, (x0 + ux * 3.2, y0 + uy * 3.2), (x1 - ux * 3.2, y1 - uy * 3.2), role, lw=1.1)
T = tri(24, 58); B = tri(64, 24)
text(ax, 24, 72.5, r'cycle $(1\,2\,3)$', 'sujet', 's')
text(ax, 64, 11.5 - 2, r'cycle $(2\,3\,4)$', 'resultat', 's')
for p, n in zip(T, (1, 2, 3)): disc(ax, p[0], p[1], 2.6, 'sujet', label=str(n), size='s')
for p, n in zip(B, (2, 3, 4)): disc(ax, p[0], p[1], 2.6, 'resultat', label=str(n), size='s')
cycle(T, 'sujet'); cycle(B, 'resultat')
for p, q in zip(T, B):
    arrow(ax, (p[0] + 2.3, p[1] - 1.6), (q[0] - 2.3, q[1] + 1.6), 'varie', lw=0.9)
text(ax, 44, 40, r'$\gamma$ renomme', 'varie', 's')
text(ax, 3, 5, r'$\gamma$ : 1 vers 2, 2 vers 3, 3 vers 4', 'fixe', 's', ha='left')
save(fig, '64-112')
