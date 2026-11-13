import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
U, OX, OY = 8, 10, 8
P = lambda x, y: (OX + U * x, OY + U * y)
for i in range(4):
    for j in range(5):
        disc(ax, *P(i, j), 0.6, 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'varie', lw=1.3)
arrow(ax, P(2, 1), P(3, 4), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(1, 3), 'sujet', lw=1.3)
disc(ax, *P(3, 4), 1.2, 'resultat')
text(ax, 24, 9.5, '$(2,1)$', 'varie', 's', ha='left')
text(ax, 15, 30, '$(1,3)$', 'sujet', 's', ha='right')
text(ax, 37, 28, '$(1,3)$', 'sujet', 's', ha='left')
text(ax, 36, 42, '$(3,4)$', 'resultat', 's', ha='left', weight='bold')
def mat(cx, cy, rows, role, cw=6.0, rh=5.6):
    w, h = 2 * cw, 2 * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        text(ax, cx, y0 + h - (i + 0.5) * rh, '    '.join(row), role, 'm')
text(ax, 72, 48.5, '$AC$', 'sujet', 'm')
mat(72, 40, [['3', '1'], ['4', '3']], 'sujet')
text(ax, 72, 28, '≠', 'resultat', 'xl', weight='bold')
mat(72, 17, [['2', '1'], ['3', '4']], 'autre')
text(ax, 72, 8, '$CA$', 'autre', 'm')
save(fig, '58-221')
