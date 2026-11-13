import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, R = 44, 35, 27
gens = {1, 5, 7, 11}
for k in range(12):
    x = cx + R * math.sin(math.radians(30 * k)); y = cy + R * math.cos(math.radians(30 * k))
    role = 'resultat' if k in gens else ('fixe' if k == 0 else 'limite')
    disc(ax, x, y, 3.4, role, label=str(k), size='s')
text(ax, cx, cy + 6, r'PGCD($k$, 12) = 1', 'resultat', 's')
text(ax, cx, cy + 1, 'vert : engendre tout', 'resultat', 's')
text(ax, cx, cy - 6, r'PGCD($k$, 12) > 1', 'limite', 's')
text(ax, cx, cy - 11, 'rouge : n’engendre pas', 'limite', 's')
save(fig, '46-124')
