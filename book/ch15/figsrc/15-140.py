import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 2.8
C = math.cos(math.radians(30))
def piece(nx, ny, nz, cx, yb, role):
    o = (cx + (ny - nx) * C * u / 2, yb)
    cubes(ax, [(i, j, k) for i in range(nx) for j in range(ny) for k in range(nz)], o, u, role)
text(ax, 44, 70, r'cube de côté $a+b$ : 3 + 2 → 8 morceaux', 'encre', 's')
# row 1: a^3 and b^3
piece(3, 3, 3, 14, 46, 'sujet'); text(ax, 30, 52, r'$a^3$ : 27', 'sujet', 's', ha='left')
piece(2, 2, 2, 56, 46, 'autre'); text(ax, 66, 52, r'$b^3$ : 8', 'autre', 's', ha='left')
# row 2: three a^2 b blocks
for k in range(3): piece(3, 3, 2, 12 + k * 17, 26, 'varie')
text(ax, 64, 31, r'3 blocs $a^2b$', 'varie', 's', ha='left'); text(ax, 64, 26, '18 chacun', 'varie', 's', ha='left')
# row 3: three a b^2 blocks
for k in range(3): piece(3, 2, 2, 12 + k * 17, 6, 'resultat')
text(ax, 64, 11, r'3 blocs $ab^2$', 'resultat', 's', ha='left'); text(ax, 64, 6, '12 chacun', 'resultat', 's', ha='left')
save(fig, '15-140')
