import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(56)
f = numberline(ax, 6, 78, 26, 0, 2, step=0.25, every=4)
for i in range(5):
    role = 'sujet' if i < 4 else 'varie'
    seg(ax, f(i * 0.25), 29, f(0.25) - f(0), 8, role)
    text(ax, f(i * 0.25 + 0.125), 33, '1/4', role, 's')
brace(ax, f(0) + 0.3, f(1) - 0.3, 38, 'fixe', '1 entier', down=False)
arrow(ax, (f(1.125), 45), (f(1.125), 38.5), 'varie')
text(ax, f(1.125), 48, 'dépasse 1', 'varie', 's')
line(ax, [(f(1.25), 24.5), (f(1.25), 15)], 'resultat', dash=True)
text(ax, f(1.25), 11, '5/4', 'resultat', 'l', weight='bold')
text(ax, 22, 11, '5 morceaux de 1/4', 'fixe', 's')
save(fig, '07-084')
