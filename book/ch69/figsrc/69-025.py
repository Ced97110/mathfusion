import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(60)
y = 36
f = numberline(ax, 8, 78, y, 0, 8, labels=False, arrow_right=False)
disc(ax, f(4), y, 1.8, 'autre')
disc(ax, f(7), y, 1.8, 'sujet')
text(ax, f(0), 31, '0', 'fixe', 's')
text(ax, f(4), 31, 'b = 4', 'autre', 's')
text(ax, f(7), 31, 'a = 7', 'sujet', 's')
arrow(ax, (f(4), y + 3), (f(7), y + 3), 'varie', curve=-0.4)
text(ax, (f(4) + f(7)) / 2, 47, '7 − 4 = 3', 'varie', 'm')
line(ax, [(f(0), 20), (f(3), 20)], 'resultat', lw=2.5)
text(ax, (f(0) + f(3)) / 2, 14.5, '3 ∈ P', 'resultat', 'm')
text(ax, 44, 56, '7 > 4', 'sujet', 'l')
save(fig, '69-025')
