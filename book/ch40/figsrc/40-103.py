import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 7                       # 1 unité = 7 mm
cx, cy = 44, 40
arrow(ax, (cx - 31, cy), (cx + 31, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 31), (cx, cy + 31), 'fixe', lw=0.6)
T = [2 * math.pi * i / 400 for i in range(401)]
line(ax, [(cx + 4 * s * math.cos(t), cy + 4 * s * math.sin(t)) for t in T], 'fixe', lw=0.9, dash=True)
line(ax, [(cx + 2 * s * math.cos(t), cy + 2 * s * math.sin(t)) for t in T], 'fixe', lw=0.9, dash=True)
line(ax, [(cx + 4 * s * math.cos(t), cy + 2 * s * math.sin(t)) for t in T], 'sujet', lw=1.5)
# étirement vertical à t = 45° : cercle de rayon 4 -> ellipse
u = math.pi / 4
xp = cx + 4 * s * math.cos(u)
arrow(ax, (xp, cy + 4 * s * math.sin(u) - 0.8), (xp, cy + 2 * s * math.sin(u) + 0.8), 'varie', lw=1.1)
disc(ax, xp, cy + 4 * s * math.sin(u), 1.0, 'fixe')
disc(ax, xp, cy + 2 * s * math.sin(u), 1.1, 'sujet')
text(ax, xp + 3, cy + 3.2 * s * math.sin(u), 'hauteur 4 → 2', 'varie', 's', ha='left') if False else None
text(ax, xp + 2, cy + 3 * s * math.sin(u) + 5, '4 → 2', 'varie', 's', ha='left')
for (x, y), lab, dx, dy, role in [((4, 0), '(4 ; 0)', 5.5, -3.5, 'sujet'), ((0, 2), '(0 ; 2)', 0, -4, 'sujet'),
                                  ((0, 4), '(0 ; 4)', 0, 3.8, 'fixe'), ((2, 0), '(2 ; 0)', 0, -3.5, 'fixe')]:
    disc(ax, cx + x * s, cy + y * s, 1.1, role)
    text(ax, cx + x * s + dx, cy + y * s + dy, lab, role, 's')
text(ax, 2, 76, 'x = 4 cos t', 'sujet', 'm', ha='left')
text(ax, 2, 70.5, 'y = 2 sin t', 'sujet', 'm', ha='left')
text(ax, 44, 8.5, 'ellipse : plus large que haute', 'sujet', 's')
text(ax, 44, 3.5, 'pointillés : cercles de rayon 4 et 2', 'fixe', 's')
save(fig, '40-103')
