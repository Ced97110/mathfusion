import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
def angle(P, deg, role, sym, name, L=26):
    q = (P[0] + L * math.cos(math.radians(deg)), P[1] + L * math.sin(math.radians(deg)))
    line(ax, [P, (P[0] + L, P[1])], role, lw=1.0); line(ax, [P, q], role, lw=1.0)
    line(ax, [(P[0] + 11 * math.cos(math.radians(t)), P[1] + 11 * math.sin(math.radians(t))) for t in range(0, int(deg) + 1, 3)], role, lw=0.9)
    text(ax, P[0] + 15 * math.cos(math.radians(deg / 2)), P[1] + 15 * math.sin(math.radians(deg / 2)) + 1, sym, role, 'xl')
    text(ax, P[0] + L / 2, P[1] - 5, name, role, 'm')
box(ax, 4, 52, 36, 11, 'fixe', label=r'$A$ et $B$ : déjà utilisés', size='s')
text(ax, 62, 57.5, 'lettres grecques', 'encre', 's')
angle((6, 22), 53.13, 'autre', r'$\alpha$', 'alpha')
angle((50, 22), 36.87, 'sujet', r'$\beta$', 'bêta')
text(ax, 63, 8, 'nom d’un angle aigu', 'sujet', 's')
save(fig, '34-123')
