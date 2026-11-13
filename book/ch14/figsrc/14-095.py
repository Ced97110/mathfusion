import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 4, 61, 'monôme : un produit', 'resultat', 'm', ha='left')
xs = [8, 32, 56]; w = 22
for x, role, s, h in [(8, 'fixe', '7', 'nombre'), (32, 'sujet', r'$x^3$', 'lettre'), (56, 'autre', r'$y^2$', 'lettre')]:
    box(ax, x, 38, w, 13, role, label=s, size='l')
    text(ax, x + w / 2, 55, h, role, 's')
for x in (30.5, 54.5): ax.plot([x + 0.5 + 0.0], [44.5], marker='x', ms=4, mew=1.2, color=COL['varie'], zorder=4)
text(ax, 4, 28, 'pas un monôme : une somme', 'limite', 'm', ha='left')
box(ax, 8, 6, 34, 13, 'fixe', label=r'$7x^3$', size='l')
box(ax, 54, 6, 22, 13, 'autre', label=r'$y^2$', size='l')
ax.plot([48], [12.5], marker='+', ms=6, mew=1.5, color=COL['limite'], zorder=4)
save(fig, '14-095')
