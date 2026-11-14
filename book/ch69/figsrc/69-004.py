import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, x1, y = 12, 76, 30
line(ax, [(x0, y), (x1, y)], 'fixe')
n = 16
pts = [x0 + (x1 - x0) * i / n for i in range(n + 1)]
for x in pts:
    disc(ax, x, y, 0.9, 'sujet')
xm = (pts[9] + pts[10]) / 2
ax.add_patch(Circle((xm, y), 1.4, ec=COL['resultat'], fc='none', ls='--', lw=0.9, zorder=4))
text(ax, x0, y - 4, '0', 'fixe', 's')
text(ax, x1, y - 4, '1', 'fixe', 's')
text(ax, 44, 38, 'essais (points bleus)', 'sujet', 's')
text(ax, 44, 47, '« pas de racine » ?', 'limite', 'm')
text(ax, xm, 17.5, 'racine non essayée ?', 'resultat', 's')
arrow(ax, (xm, 20), (xm, y - 2.8), 'resultat', lw=0.9)
save(fig, '69-004')
