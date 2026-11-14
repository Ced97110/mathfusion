import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$\frac{1}{x}$', 'sujet', 'xl')
y = 22
f = numberline(ax, 10, 70, y, -4, 4, every=2, arrow_right=True)
for v, lab in ((-4, r'$-\frac{1}{4}$'), (4, r'$\frac{1}{4}$')):
    ax.add_patch(Circle((f(v), y), 1.5, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
    text(ax, f(v), y + 7, lab, 'resultat', 's')
disc(ax, f(0), y, 1.6, 'limite')
line(ax, [(f(0) - 1.1, y - 1.1), (f(0) + 1.1, y + 1.1)], 'limite', lw=1.2); line(ax, [(f(0) - 1.1, y + 1.1), (f(0) + 1.1, y - 1.1)], 'limite', lw=1.2)
text(ax, f(0), y + 8, r'$\frac{1}{0}$ : écarté', 'limite', 's')
save(fig, '17-124')
