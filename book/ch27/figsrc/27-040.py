import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(62)
k = 6.4; ax0, y0 = 8, 30
Ap = (ax0, y0); Hp = (ax0 + 5 * k, y0); Gp = (ax0 + 5 * k, y0 + 2 * k)
poly(ax, [Ap, Hp, Gp], 'fixe')
line(ax, [Ap, Gp], 'sujet', 1.8); line(ax, [Ap, Hp], 'resultat', 1.8); line(ax, [Hp, Gp], 'fixe', 1.0)
line(ax, [(Hp[0] - 1.8, y0), (Hp[0] - 1.8, y0 + 1.8), (Hp[0], y0 + 1.8)], 'encre', 0.8)
ax.add_patch(Arc(Ap, 14, 14, theta1=0, theta2=21.8, color=COL['varie'], lw=1.2, zorder=3))
text(ax, ax0 - 1, y0 - 4, 'A', 'fixe'); text(ax, Hp[0] + 1, y0 - 4, 'H', 'fixe'); text(ax, Gp[0] + 1, Gp[1] + 3.5, 'G', 'sujet')
text(ax, ax0 + 11, y0 + 1.8, r'$\alpha$', 'varie', 's', ha='left')
text(ax, 62, 46, 'câble AG', 'sujet', 's', ha='left')
text(ax, 62, 39, 'projeté AH', 'resultat', 's', ha='left')
# trois actions
y = 11; w = 24
box(ax, 2, y, w, 11, 'sujet', label='AG = 5,385', size='s')
text(ax, 2 + w + 3, y + 5.5, r'$\times$', 'encre', 'l')
box(ax, 2 + w + 6, y, w, 11, 'varie', label=r'cos $\alpha$ = 0,9285', size='s')
text(ax, 2 + 2 * w + 9, y + 5.5, '=', 'encre', 'l')
box(ax, 2 + 2 * w + 12, y, 88 - 2 - (2 + 2 * w + 12), 11, 'resultat', label='AH = 5', size='s')
save(fig, '27-040')
