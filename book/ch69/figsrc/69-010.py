import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(46)
y = 28
f = numberline(ax, 8, 78, y, -3, 3, labels=False, arrow_right=False)
box(ax, f(-3), y + 3, f(0) - f(-3) - 0.6, 8, 'autre', label='N : les négatifs')
box(ax, f(0) + 0.6, y + 3, f(3) - f(0) - 0.6, 8, 'resultat', label='P : les positifs')
disc(ax, f(-2), y, 1.8, 'sujet')
disc(ax, f(0), y, 1.8, 'fixe')
arrow(ax, (f(-2), y - 2.6), (f(-2), 19.5), 'fixe')
arrow(ax, (f(0), y - 2.6), (f(0), 19.5), 'fixe')
text(ax, f(-2), 16, '−2 ∈ N', 'resultat', 'm')
text(ax, f(0) + 4, 16, '0 ∉ N et 0 ∉ P', 'resultat', 'm', ha='left')
save(fig, '69-010')
