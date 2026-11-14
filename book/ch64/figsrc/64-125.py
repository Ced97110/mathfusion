import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 9
def tri(cx, cy):   # sommets : haut, bas-droite, bas-gauche
    return [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, -30, 210)]
def cycle(P, role):
    for i in range(3):
        (x0, y0), (x1, y1) = P[i], P[(i + 1) % 3]
        d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
        arrow(ax, (x0 + ux * 3.2, y0 + uy * 3.2), (x1 - ux * 3.2, y1 - uy * 3.2), role, lw=1.1)
fig, ax = canvas(100)
gamma = {1: 2, 2: 1, 3: 4, 4: 3}
left = [1, 3, 2]                      # (1 2 3)^2 = (1 3 2)
right = [gamma[v] for v in left]      # (2 4 1) = (1 2 4)
T = tri(24, 76); B = tri(64, 44)
for p, n in zip(T, left): disc(ax, p[0], p[1], 2.6, 'sujet', label=str(n), size='s')
for p, n in zip(B, right): disc(ax, p[0], p[1], 2.6, 'resultat', label=str(n), size='s')
cycle(T, 'sujet'); cycle(B, 'resultat')
for p, q in zip(T, B):
    arrow(ax, (p[0] + 2.3, p[1] - 1.6), (q[0] - 2.3, q[1] + 1.6), 'varie', lw=0.9)
text(ax, 24, 92, r'$(1\,2\,3)^2=(1\,3\,2)$ dans $N$', 'sujet', 's')
text(ax, 64, 31, r'$(2\,4\,1)=(1\,2\,4)$ dans $N$', 'resultat', 's')
text(ax, 44, 61, r'$\gamma$ renomme', 'varie', 's')
text(ax, 3, 22, r'$\gamma=(1\,2)(3\,4)$ : 2 échanges, paire', 'fixe', 's', ha='left')
box(ax, 3, 2, 40, 10, 'resultat', label=r'tous les 3-cycles dans $N$', size='s')
arrow(ax, (44, 7), (51, 7), 'resultat')
box(ax, 52, 2, 33, 10, 'sujet', label=r'donc $A_n$ dans $N$', size='s')
save(fig, '64-125')
