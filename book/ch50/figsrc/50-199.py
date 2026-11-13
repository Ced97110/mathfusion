import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs, x0 = 5.0, 22.0
text(ax, 44, 56, r'$|Z(G)|$ divise $p^2$', 'encre', 'l')
for yb, n, role, lab, rl in [(42, 1, 'limite', '1', 'exclu'), (30, 3, 'resultat', r'$p=3$', 'possible'), (18, 9, 'resultat', r'$p^2=9$', 'possible')]:
    for i in range(n):
        ax.add_patch(Rectangle((x0 + i * cs, yb), cs, 6, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, 12, yb + 3, lab, 'encre', 'm'); text(ax, 77, yb + 3, rl, role, 's')
text(ax, 44, 8, r'le centre a plus que $e$', 'fixe', 's')
save(fig, '50-199')
