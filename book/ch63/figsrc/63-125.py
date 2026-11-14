import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(104)

def sets(cy, h, n_left, n_right, lrole, rrole, tl, tr):
    ax.add_patch(Ellipse((18, cy), 26, h, ec=COL[lrole], fc=FILL[lrole], lw=1.0, zorder=1))
    ax.add_patch(Ellipse((70, cy), 26, h, ec=COL[rrole], fc=FILL[rrole], lw=1.0, zorder=1))
    text(ax, 18, cy + h / 2 + 4, tl, lrole, 's')
    text(ax, 70, cy + h / 2 + 4, tr, rrole, 's')
    def ys(n):
        return [cy + (i - (n - 1) / 2) * 7 for i in reversed(range(n))]
    L, Rr = ys(n_left), ys(n_right)
    for y in L: disc(ax, 18, y, 2, lrole)
    for y in Rr: disc(ax, 70, y, 2, rrole)
    return L, Rr

# top: the Galois example, 5 matched pairs
L, Rr = sets(78, 40, 5, 5, 'sujet', 'autre', r'$\Gamma$ : 5 sous-groupes', r'$\Sigma$ : 5 corps')
for a, b in zip(L, Rr):
    arrow(ax, (21, a), (67, b), 'resultat', lw=0.8, both=True)
text(ax, 44, 52.5, r'$\mathbb{Q}(\sqrt{2},\sqrt{3})/\mathbb{Q}$ : bijection', 'resultat', 's')
text(ax, 44, 46.5,r'$H\mapsto\mathrm{Inv}\,H$ et $K\mapsto\mathrm{Gal}(E/K)$', 'resultat', 's')
# bottom: Q(r)/Q, no bijection
L2, R2 = sets(24, 26, 1, 2, 'sujet', 'autre', r'$\Gamma$ : 1', r'$\Sigma$ : 2')
text(ax, 18, L2[0] - 0.2 + 0, r'$\{1\}$', 'sujet', 's', ha='right')
ax.texts[-1].set_x(13.5)
for y, l in zip(R2, [r'$\mathbb{Q}(r)$', r'$\mathbb{Q}$']):
    text(ax, 74, y, l, 'autre', 's', ha='left')
for y in R2:
    arrow(ax, (67, y), (21, L2[0]), 'limite', lw=0.8)
text(ax, 44, 4, r'$\mathbb{Q}(r)/\mathbb{Q}$ : 1 ≠ 2, pas de bijection', 'limite', 's')
save(fig, '63-125')
