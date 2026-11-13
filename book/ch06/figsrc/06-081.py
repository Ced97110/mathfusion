import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(x, y, wd, ht, role, lw=0.5):
    ax.add_patch(Rectangle((x, y), wd, ht, ec=COL[role], fc=FILL[role], lw=lw, zorder=2))
fig, ax = canvas(58)
c, ox, oy = 4, 4, 9
for n in range(100):
    r, k = divmod(n, 10)
    cell(ox + k * c, oy + (9 - r) * c, c, c, 'sujet' if n < 75 else 'fixe')
text(ax, 24, 54, '1 euro = 100 centimes', 'fixe', 's')
text(ax, 24, 4, '75 cases sur 100', 'sujet', 's')
text(ax, 67, 42, '0,75', 'sujet', 'xl')
text(ax, 67, 29, r'$=\ \frac{75}{100}$', 'sujet', 'xl')
text(ax, 67, 14, r'$=\ \frac{3}{4}$', 'resultat', 'xl')
save(fig, '06-081')
