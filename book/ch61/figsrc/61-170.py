import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, k = 44, 29, 12
arrow(ax, (ox - 32, oy), (ox + 32, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy - 26), (ox, oy + 30), 'fixe', lw=0.7)
text(ax, ox + 33, oy - 3, '$x$', 'fixe', 's'); text(ax, ox + 3, oy + 30, '$y$', 'fixe', 's')
ax.add_patch(Circle((ox, oy), 2 * k, ec=COL['sujet'], fc='none', lw=1.3, zorder=2))
line(ax, [(ox - 2.4 * k, oy - 1.4 * k), (ox + 1.4 * k, oy + 2.4 * k)], 'varie', lw=1.3)
s7 = math.sqrt(7)
for x in ((-1 + s7) / 2, (-1 - s7) / 2):
    y = x + 1
    line(ax, [(ox + x * k, oy + y * k), (ox + x * k, oy)], 'fixe', lw=0.6, dash=True)
    disc(ax, ox + x * k, oy + y * k, 1.0, 'resultat')
text(ax, ox + 0.823 * k + 1, oy - 4, '≈ 0,82', 'resultat', 's', ha='left')
text(ax, ox - 1.823 * k - 1, oy + 4, '≈ −1,82', 'resultat', 's', ha='right')
text(ax, 72, 14, '$x^2+y^2=4$', 'sujet', 's'); text(ax, 74, 56, '$y=x+1$', 'varie', 's')
text(ax, 72, 7, r'même $\sqrt{7}$', 'resultat', 's')
save(fig, '61-170')
