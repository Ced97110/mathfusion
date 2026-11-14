import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
c = (44, 44); r = 22
ax.add_patch(Circle(c, r, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))
line(ax, [(c[0] - 26, c[1]), (c[0] + 26, c[1])], 'fixe', lw=0.6); line(ax, [(c[0], c[1] - 26), (c[0], c[1] + 26)], 'fixe', lw=0.6)
p1 = (c[0] + 0.8 * r, c[1] + 0.6 * r); p2 = (c[0] - 0.8 * r, c[1] + 0.6 * r)
for p, role in ((p1, 'resultat'), (p2, 'autre')):
    line(ax, [c, p], role, lw=1.4)
    line(ax, [p, (p[0], c[1])], role, dash=True); line(ax, [(p[0], c[1]), c], role, dash=True)
    disc(ax, p[0], p[1], 1.5, role)
text(ax, 52, 53.5, '1', 'sujet', 's')
text(ax, 64, 61, '(0,8 ; 0,6)', 'resultat', 's', ha='left'); text(ax, 24, 61, '(−0,8 ; 0,6)', 'autre', 's', ha='right')
text(ax, 22, 12, '0,6 ÷ (−0,8) = −0,75', 'autre', 's'); text(ax, 66, 12, '0,6 ÷ 0,8 = 0,75', 'resultat', 's')
text(ax, 44, 4.5, r'$y \, / \, x$ : hauteur ÷ abscisse', 'sujet', 's')
save(fig, '25-137')
