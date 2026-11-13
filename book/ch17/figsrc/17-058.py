import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r, role, label=None, size='s'):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=4))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(52)
y = 24
f = numberline(ax, 8, 68, y, 0, 16, step=16, labels=False, arrow_right=False)
for v in (3, 7): dot(ax, f(v), y, 2.3, 'sujet', label=str(v), size='s')
for v in (11, 15): dot(ax, f(v), y, 2.3, 'resultat', label=str(v), size='s')
brace(ax, f(3), f(7), y - 4, 'sujet', 'écart 4', down=True)
brace(ax, f(11), f(15), y - 4, 'resultat', 'écart 4', down=True)
arrow(ax, (f(7) + 4, y + 7), (f(11) - 4, y + 7), 'varie', lw=1.2)
text(ax, (f(7) + f(11)) / 2, y + 11, '+ 8 aux deux', 'varie', 's')
text(ax, (f(3) + f(7)) / 2, y + 7, '3 < 7', 'sujet', 's')
text(ax, (f(11) + f(15)) / 2 + 3, y + 7, '11 < 15', 'resultat', 's')
text(ax, 44, 4, 'l’écart ne change pas', 'fixe', 's')
save(fig, '17-058')
