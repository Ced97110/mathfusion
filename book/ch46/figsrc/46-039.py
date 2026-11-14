import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(88)
cx, cy, R = 44, 42, 22
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls=':'))
P = {0: (cx + R, cy), 1: (cx, cy + R), 2: (cx - R, cy), 3: (cx, cy - R)}
def pt(k, d): return (cx + d * math.cos(math.pi * k / 2 + 0.0), cy + d * math.sin(math.pi * k / 2))
for k, (x, y) in P.items(): disc(ax, x, y, 2.4, 'sujet')
text(ax, P[0][0] + 3, P[0][1] + 5, r'$i^4 = 1$', 'sujet', 'm', ha='right')
text(ax, P[1][0], P[1][1] + 6, r'$i$', 'sujet', 'm')
text(ax, P[2][0] - 3, P[2][1] + 5, r'$i^2 = -1$', 'sujet', 'm', ha='left')
text(ax, P[3][0], P[3][1] - 6, r'$i^3 = -i$', 'sujet', 'm')
for k in range(4):
    a0 = math.pi * k / 2 + 0.38; a1 = math.pi * (k + 1) / 2 - 0.38
    arrow(ax, (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1)), 'varie', curve=0.25)
text(ax, cx, cy + 3, r'$\times\, i$', 'varie', 'l'); text(ax, cx, cy - 3, 'à chaque flèche', 'varie', 's')
text(ax, 44, 8, '4 nombres : tout produit reste dedans', 'resultat', 's')
save(fig, '46-039')
