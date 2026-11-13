import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
D = -14  # vertical shift
vals = ['2', '1', '−1']; bh = 8.5
text(ax, 23, 97 + D, 'GL₂(ℝ)', 'sujet', 'l'); text(ax, 74, 97 + D, 'ℝ*', 'autre', 'l')
box(ax, 2, 61 + D, 42, 3 * bh + 2 * 1.5 + 4, 'fixe', fill=False, dash=True)
for i, v in enumerate(vals):
    y = 82 + D - i * (bh + 1.5)
    ker = v == '1'
    box(ax, 5, y, 36, bh, 'resultat' if ker else 'sujet', label=('det = 1 : SL₂(ℝ)' if ker else 'det = ' + v), size='s')
    disc(ax, 74, y + bh / 2, 3.4, 'resultat' if ker else 'autre', label=v, size='s')
    arrow(ax, (41, y + bh / 2), (70.2, y + bh / 2), 'resultat' if ker else 'varie')
text(ax, 44, 54 + D, 'GL₂/SL₂ ≅ ℝ*', 'resultat', 'l')
mats = ['1 1\n0 1\ndet 1', '1 0\n1 1\ndet 1', '2 1\n1 1\ndet 1']
for x, m in zip([4, 34, 64], mats):
    box(ax, x, 26 + D, 22, 16, 'resultat', label=m, size='s')
yc = 34 + D
line(ax, [(28, yc - 2), (32, yc + 2)], 'varie'); line(ax, [(28, yc + 2), (32, yc - 2)], 'varie')
line(ax, [(57.5, yc + 1.2), (62.5, yc + 1.2)], 'varie'); line(ax, [(57.5, yc - 1.2), (62.5, yc - 1.2)], 'varie')
text(ax, 44, 19 + D, 'le produit reste dans SL₂(ℝ)', 'resultat', 's')
save(fig, '48-137')
