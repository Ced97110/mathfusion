import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, 'somme 6 : son tiers vaut 2', 'sujet', 's')
yt, yb = 52, 18
f = numberline(ax, 8, 72, yt, -2, 3, step=1, labels=False, arrow_right=False)
numberline(ax, 8, 72, yb, -2, 3, step=1, labels=False, arrow_right=False)
text(ax, 4, yt + 6, r'$x$', 'sujet', 's')
text(ax, 4, yb + 6, r'$y$', 'resultat', 's')
def dsk(x, y, role, lab):
    ax.add_patch(Circle((x, y), 3.4, ec=COL[role], fc=FILL[role], lw=0.8, zorder=3.5))
    text(ax, x, y, lab, role, 's')
for v in (1, 2, 3):
    dsk(f(v), yt, 'sujet', str(v))
    dsk(f(v - 2), yb, 'resultat', str(v - 2).replace('-', '−'))
    arrow(ax, (f(v), yt - 4.2), (f(v - 2), yb + 4.2), 'varie')
text(ax, 3, 36, r'$y=x-2$', 'varie', 's', ha='left')
text(ax, 44, 8, r'somme $0$ : $y^3-y=0$', 'resultat', 's')
save(fig, '65-110')
