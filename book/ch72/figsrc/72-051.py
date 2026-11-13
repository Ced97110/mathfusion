import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
labs = [('plan hyperbolique', 'sujet'), (r'base $(u,v)$ : paire hyp.', 'autre'), (r'discriminant $=-1$', 'resultat')]
ys = [74, 40, 6]
for (l, r), y in zip(labs, ys):
    box(ax, 2, y, 48, 14, r, label=l, size='s')
for y in (40, 6):
    arrow(ax, (26, y + 14.6), (26, y + 33.4), 'fixe', both=True)
    text(ax, 28, y + 24, 'équivalents', 'fixe', 's', ha='left')
# right column: the plane with the basis, the table, the computation
cx, cy, k = 69, 76, 9
arrow(ax, (cx - 13, cy), (cx + 14, cy), 'fixe', lw=0.6); arrow(ax, (cx, cy - 13), (cx, cy + 12), 'fixe', lw=0.6)
arrow(ax, (cx, cy), (cx + k, cy + k), 'autre', lw=1.4)
line(ax, [(51, 81), (cx - 14, 81)], 'sujet', lw=0.7, dash=True)
arrow(ax, (cx, cy), (cx + k / 2, cy - k / 2), 'autre', lw=1.4)
text(ax, cx + k + 2.5, cy + k - 1, r'$u$', 'autre', 'm')
text(ax, cx + k / 2 + 3.5, cy - k / 2 - 1, r'$v$', 'autre', 'm')
x0, y0, c = 58, 33, 10
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, 'autre', fill=True)
for (i, j, t) in ((0, 0, '0'), (0, 1, '1'), (1, 0, '1'), (1, 1, '0')):
    text(ax, x0 + (j + 0.5) * c, y0 + (1.5 - i) * c, t, 'autre', 'l')
line(ax, [(51, 47), (x0 - 1, 47)], 'autre', lw=0.7, dash=True)
text(ax, 69, 13, r'$0\times0-1\times1$', 'resultat', 'm')
text(ax, 69, 6.5, r'$=-1$', 'resultat', 'l')
line(ax, [(51, 13), (55, 13)], 'resultat', lw=0.7, dash=True)
save(fig, '72-051')
