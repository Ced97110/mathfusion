import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
k = 5.5
O = (44, 38)
v = (3, 4)
assert math.hypot(*v) == 5
T = lambda q: (O[0] + k * q[0], O[1] + k * q[1])
ax.add_patch(Circle(O, 5 * k, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
arrow(ax, O, T(v), 'autre', lw=1.8)
arrow(ax, O, T((-3, -4)), 'sujet', lw=1.8)
disc(ax, O[0], O[1], 0.9, 'encre')
text(ax, T(v)[0] + 2, T(v)[1] + 3, r'$v=\langle 3;\ 4\rangle$', 'autre', 's', ha='left')
text(ax, 20, 5, r'$-v=\langle -3;\ -4\rangle$', 'sujet', 's', ha='left')
text(ax, 80, 52, 'même norme 5', 'fixe', 's', ha='right')
text(ax, 84, 38, 'vecteur nul', 'encre', 's', ha='right')
arrow(ax, (66, 38), (O[0] + 2, O[1]), 'encre', lw=0.6)
save(fig, '41-056')
