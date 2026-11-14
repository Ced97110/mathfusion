import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(54)
y = 16
f = numberline(ax, 10, 78, y, -2, 2, arrow_right=False)
for v in (1, 2):
    disc(ax, f(v), y, 1.8, 'resultat')
disc(ax, f(0), y, 1.8, 'fixe')
disc(ax, f(0.5), y, 1.8, 'varie')
disc(ax, f(-0.5), y, 1.8, 'varie', fill=False)
text(ax, f(0.5), 21, '½', 'varie', 's')
text(ax, f(-0.5), 21, '−½', 'varie', 's')
text(ax, 44, 50, 'P = {1, 2, 3, …}', 'resultat', 'm')
text(ax, 44, 41, '½ ∈ P : faux', 'limite', 's')
text(ax, 44, 35, '½ = 0 : faux', 'limite', 's')
text(ax, 44, 29, '−½ ∈ P : faux', 'limite', 's')
save(fig, '69-020')
