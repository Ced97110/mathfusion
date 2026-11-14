import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$x=1$ : $f=y^2-3$, $g=y+1$', 'encre', 'm')
rows = [('f', 'sujet', [1, 0, -3]), ('g', 'autre', [1, 1, 0]), ('g', 'autre', [0, 1, 1])]
w, h, gap, x0 = 14, 9, 1.5, 20
for r, (name, role, vals) in enumerate(rows):
    y = 38 - r * (h + gap)
    text(ax, 11, y + h / 2, name, role, 'l')
    for c, v in enumerate(vals):
        box(ax, x0 + c * (w + gap), y, w, h, role if v != 0 else 'fixe', label=str(v).replace('-', '−'), size='m')
yt, yb = 38 + h, 38 - 2 * (h + gap)
xb = x0 + 3 * (w + gap) + 1.5
line(ax, [(xb - 1.5, yt), (xb, yt), (xb, yb), (xb - 1.5, yb)], 'resultat')
text(ax, xb + 9, (yt + yb) / 2, r'$m+n=3$', 'resultat', 'm')
text(ax, 44, 8, "chaque ligne de $g$ glisse", 'varie', 's')
save(fig, '70-079')
