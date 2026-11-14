import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda v: 44 + v * 4.6
R = list(range(-8, 9))
def row(y, pred, role, lab, lab_role=None):
    line(ax, [(X(-8), y), (X(8), y)], 'fixe', lw=0.5)
    for v in R:
        if pred(v): disc(ax, X(v), y, 1.6, role)
        else: disc(ax, X(v), y, 0.5, 'fixe')
    text(ax, 2, y + 5, lab, lab_role or role, 'm', ha='left')
text(ax, 44, 76, r'les sous-groupes de ℤ : les $s$ℤ', 'encre', 'm')
row(62, lambda v: v == 0, 'sujet', '0ℤ = {0}')
row(48, lambda v: v % 2 == 0, 'sujet', '2ℤ')
row(34, lambda v: v % 3 == 0, 'sujet', '3ℤ')
row(18, lambda v: v % 2 != 0, 'limite', r'impairs : sans 0, pas de $s$ℤ')
ax.add_patch(Circle((X(0), 18), 1.6, ec=COL['limite'], fc='none', lw=0.8, ls='--', zorder=3))
text(ax, X(0), 11, '0', 'fixe', 's')
text(ax, X(-6), 11, '−6', 'fixe', 's')
text(ax, X(6), 11, '6', 'fixe', 's')
save(fig, '46-115')
