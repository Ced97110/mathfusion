import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 8, 46, 72, 12, 'sujet', label=r'après $F_i$ : point suivant', size='m')
cxs = [16, 44, 72]; cy = 24
for cx in cxs: arrow(ax, (cx, 46), (cx, 37), 'fixe')
# two lines
line(ax, [(16 - 10, cy - 8), (16 + 10, cy + 8)], 'sujet', lw=1.2); line(ax, [(16 - 10, cy + 8), (16 + 10, cy - 8)], 'varie', lw=1.2)
disc(ax, 16, cy, 1.0, 'resultat')
# line + circle
c = 44; ax.add_patch(Circle((c, cy), 8, ec=COL['sujet'], fc='none', lw=1.2, zorder=2))
line(ax, [(c - 10, cy - 4), (c + 10, cy + 6)], 'varie', lw=1.2)
d = math.sqrt(316) / 2.5
for dx in ((-1 + math.sqrt(316)) / 2.5, (-1 - math.sqrt(316)) / 2.5): disc(ax, c + dx, cy + 0.5 * dx + 1, 1.0, 'resultat')
# two circles
c = 72
ax.add_patch(Circle((c - 4, cy), 8, ec=COL['sujet'], fc='none', lw=1.2, zorder=2)); ax.add_patch(Circle((c + 4, cy), 8, ec=COL['varie'], fc='none', lw=1.2, zorder=2))
for s in (1, -1): disc(ax, c, cy + s * math.sqrt(48), 1.0, 'resultat')
for cx, l in zip(cxs, ['deux droites', 'droite et cercle', 'deux cercles']): text(ax, cx, 8, l, 'encre', 's')
save(fig, '61-172')
