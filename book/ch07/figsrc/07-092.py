import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(76)
rows = [(66, 'saison 1', [1, 0], 'sujet', '1/2'), (54, 'saison 2', [1, 0, 0], 'autre', '1/3')]
for y, lab, res, role, fr in rows:
    text(ax, 2, y + 3, lab, role, 's', ha='left')
    for i, v in enumerate(res): seg(ax, 26 + i * 8, y, 7, 6, role if v else 'fixe')
    text(ax, 80, y + 3, fr, role, 'm', weight='bold')
text(ax, 2, 42, 'total', 'resultat', 's', ha='left')
cells = [('sujet', 1), ('fixe', 0), ('autre', 1), ('fixe', 0), ('fixe', 0)]
for i, (role, v) in enumerate(cells): seg(ax, 26 + i * 8, 39, 7, 6, role)
text(ax, 80, 42, '2/5', 'resultat', 'm', weight='bold')
f = numberline(ax, 6, 78, 20, 0, 1, arrow_right=False)
for v, lab, role, dy in [(1 / 3, '1/3', 'autre', -8), (0.4, '2/5', 'resultat', 6), (0.5, '1/2', 'sujet', -8)]:
    disc(ax, f(v), 20, 1.3, role); text(ax, f(v), 20 + dy, lab, role, 's', weight='bold')
save(fig, '07-092')
