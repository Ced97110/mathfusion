import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
# gauche : ℤ/12ℤ engendré par 1
cx, cy, R = 22, 34, 12
text(ax, 22, 60, 'ℤ/12ℤ : cyclique', 'sujet', 's', weight='bold')
pts = []
for k in range(12):
    a = math.pi / 2 - 2 * math.pi * k / 12
    pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for k, (x, y) in enumerate(pts):
    disc(ax, x, y, 1.9 if k else 2.6, 'sujet' if k in (0, 1) else 'fixe')
for k in (0, 1, 2):
    x, y = pts[k]
    text(ax, cx + (R + 5.5) * math.cos(math.pi / 2 - 2 * math.pi * k / 12), cy + (R + 5.5) * math.sin(math.pi / 2 - 2 * math.pi * k / 12), str(k), 'sujet', 's')
arrow(ax, (pts[0][0] + 2, pts[0][1] - 1), (pts[1][0] - 2, pts[1][1] + 1.2), 'varie', lw=1.2)
text(ax, 22, 15, 'engendré par 1 :', 'varie', 's')
text(ax, 22, 10.5, '1, 1 + 1, 1 + 1 + 1, …', 'varie', 's')
# droite : somme directe
text(ax, 66, 60, 'module de type fini M', 'sujet', 's', weight='bold')
for i, r in enumerate(('sujet', 'varie', 'autre')):
    box(ax, 50 + i * 12.5, 34, 11.5, 12, r, label=f'C{"₁₂₃"[i]}', size='m')
brace(ax, 50, 50 + 3 * 12.5 - 1, 33, 'fixe', label='M = C₁ ⊕ C₂ ⊕ …', down=True)
text(ax, 68, 17, 'chaque C est cyclique', 'fixe', 's')
box(ax, 44, 2, 42, 8, 'resultat', label='somme directe de cycliques', size='s')
save(fig, '58-330')
