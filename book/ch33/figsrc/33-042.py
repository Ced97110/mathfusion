import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(70); cx, cy, R = 30, 30, 16; yh = cy + 0.5 * R
halves(ax, cx, cy, R)
ax_x = 9
line(ax, [(ax_x, cy - R), (ax_x, cy + 2 * R + 2)], 'fixe', 0.7)
for v, y, r in [(1, cy + R, 'fixe'), (0.5, yh, 'varie'), (2, cy + 2 * R, 'limite')]:
    line(ax, [(ax_x - 1, y), (ax_x + 1, y)], r, 0.8); text(ax, ax_x - 3.6, y, f'{v:g}'.replace('.', ','), r, 's')
line(ax, [(ax_x, yh), (cx + R + 1, yh)], 'varie', 1.0)
p = P(cx, cy, R, 30); line(ax, [(cx, cy), p], 'resultat', 1.0); dot(ax, *p, 'resultat')
arc(ax, cx, cy, 8, 0, 30, 'resultat', 1.2); text(ax, cx + 12.5, cy + 2.4, '30°', 'resultat', 's')
text(ax, p[0] + 2.5, yh + 3.2, '3', 'sujet', 's', weight='bold'); text(ax, cx + R + 3.4, yh, '2', 'sujet', 's', weight='bold')
line(ax, [(ax_x, cy + 2 * R), (cx + 14, cy + 2 * R)], 'limite', 1.0, True); text(ax, cx + 16, cy + 2 * R, '1', 'sujet', 's', weight='bold')
text(ax, cx + 20, cy + 2 * R, 'x = 2 : aucun point', 'limite', 's', ha='left') if False else text(ax, cx + 19.5, cy + 2 * R, 'aucun point', 'limite', 's', ha='left')
for y, s in [(45, '1  vérifier −1 ≤ x ≤ 1'), (30, '2  point à hauteur 0,5'), (15, '3  lire l’angle : 30°')]:
    box(ax, 50, y, 36, 10, 'sujet', label=s, size='s')
arrow(ax, (68, 45), (68, 40.5), 'fixe'); arrow(ax, (68, 30), (68, 25.5), 'fixe')
save(fig, '33-042')
