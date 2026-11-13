import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
groups = [('2', 36), ('3', 56), ('x', 76)]
pitch, r = 6, 2.5
text(ax, 2, 87, 'facteurs :', 'fixe', 's', ha='left')
for g, cx in groups:
    box(ax, cx - 8, 80, 16, 9, 'fixe', label=g if g != 'x' else r'$x$', size='l', weight='bold')
def row(y, lab, exps, role):
    text(ax, 28, y, lab, role, 's', ha='right')
    for (g, cx), n in zip(groups, exps):
        for k in range(n):
            if role == 'resultat':
                ax.add_patch(Circle((cx - pitch / 2 + k * pitch, y), r, ec=COL[role], fc=FILL['encre'], lw=1.2, zorder=3))
            else:
                disc(ax, cx - pitch / 2 + k * pitch, y, r, role)
def ppcm(a, b): return [max(p, q) for p, q in zip(a, b)]
e12, e18 = [2, 1, 0], [1, 2, 0]
text(ax, 2, 75, 'nombres', 'fixe', 's', ha='left', weight='bold')
box(ax, 2, 49.5, 84, 8, 'resultat', r=0.8)
row(69, '12', e12, 'sujet'); row(61, '18', e18, 'autre'); row(53.5, 'PPCM 36', ppcm(e12, e18), 'resultat')
line(ax, [(2, 45), (86, 45)], 'fixe', lw=0.5)
ea, eb = [1, 1, 2], [2, 0, 1]
text(ax, 2, 41, r'avec une lettre $x$', 'fixe', 's', ha='left', weight='bold')
box(ax, 2, 12.5, 84, 8, 'resultat', r=0.8)
row(33, r'$6x^2$', ea, 'sujet'); row(25, r'$4x$', eb, 'autre'); row(16.5, r'PPCM $12x^2$', ppcm(ea, eb), 'resultat')
text(ax, 2, 4, '1 pastille = 1 facteur', 'fixe', 's', ha='left')
text(ax, 86, 4, 'plus grand nombre gardé', 'resultat', 's', ha='right')
save(fig, '05-186')
