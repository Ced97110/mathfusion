import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(58)
y = 26
f = numberline(ax, 6, 76, y, 0, 56, step=56, labels=False, arrow_right=False)
text(ax, f(0), y - 4, '0', 'fixe', 's')
for v in (3, 7): dot(ax, f(v), y, 1.4, 'sujet')
for v in (24, 56): dot(ax, f(v), y, 1.4, 'resultat')
for v in (3, 7): text(ax, f(v), y + 4, str(v), 'sujet', 's')
for v in (24, 56): text(ax, f(v), y + 4, str(v), 'resultat', 's')
arrow(ax, (f(7) + 4, y + 11), (f(24) - 4, y + 11), 'varie', lw=1.2)
text(ax, (f(7) + f(24)) / 2, y + 15, r'$\times 8$ aux deux', 'varie', 's')
brace(ax, f(3), f(7), y - 7, 'sujet', 'écart 4', down=True)
brace(ax, f(24), f(56), y - 7, 'resultat', 'écart 32', down=True)
text(ax, 44, 52, r'$3 < 7$ donne $24 < 56$', 'resultat', 'm')
save(fig, '17-062')
