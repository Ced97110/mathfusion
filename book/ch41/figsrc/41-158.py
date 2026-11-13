import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
# quatre outils du chapitre, un cadre chacun
cw, ch = 40, 38
cells = [(4, 48), (46, 48), (4, 6), (46, 6)]
for (x, y) in cells:
    box(ax, x, y, cw, ch, 'fixe', lw=0.6)
# 1 cosinus et sinus : 50 et 86,60 (angle de 60 degrés)
x, y = cells[0]; a = math.radians(60)
ex, ey = 20, 20  # longueur de l'hypoténuse : 20 mm
bx, by = x + 6, y + 8
tipx, tipy = bx + ex * math.cos(a), by + ex * math.sin(a)
line(ax, [(bx, by), (tipx, by), (tipx, tipy)], 'varie')
arrow(ax, (bx, by), (tipx, tipy), 'sujet', lw=1.3)
text(ax, (bx + tipx) / 2, by - 3, '50', 'varie', 's')
text(ax, tipx + 5, (by + tipy) / 2, '86,60', 'varie', 's')
text(ax, x + 20, y + ch - 3.5, 'cosinus, sinus', 'encre', 's')
# 2 cercle unité : signes
x, y = cells[1]; cx, cy, r = x + 20, y + 16, 11
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.8, zorder=2))
line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe', lw=0.6)
line(ax, [(cx, cy - r - 3), (cx, cy + r + 3)], 'fixe', lw=0.6)
text(ax, x + 20, y + ch - 3.5, 'cercle unité : signes', 'encre', 's')
text(ax, cx + 6, cy + 6, '+ +', 'resultat', 's')
text(ax, cx - 6, cy - 6, '− −', 'fixe', 's')
# 3 arctangente : direction
x, y = cells[2]; bx, by = x + 6, y + 9
arrow(ax, (bx, by), (bx + 28, by + 14), 'sujet', lw=1.3)
line(ax, [(bx, by), (bx + 30, by)], 'fixe', lw=0.6)
pts = [(bx + 14 * math.cos(math.atan2(14, 28) * i / 12), by + 14 * math.sin(math.atan2(14, 28) * i / 12)) for i in range(13)]
line(ax, pts, 'varie')
text(ax, x + 20, y + ch - 3.5, 'arctangente', 'encre', 's')
# 4 loi des cosinus : triangle u, v, u - v
x, y = cells[3]
A, B, C = (x + 6, y + 8), (x + 34, y + 8), (x + 16, y + 24)
poly(ax, [A, B, C], 'autre')
text(ax, x + 20, y + ch - 3.5, 'loi des cosinus', 'encre', 's')
text(ax, (A[0] + B[0]) / 2, y + 4.2, r'$u$', 'sujet', 's')
text(ax, x + 7.5, y + 18, r'$v$', 'autre', 's')
text(ax, x + 31, y + 18, r'$u-v$', 'autre', 's')
save(fig, '41-158')
