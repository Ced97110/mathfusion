import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(58)
y = 28
f = numberline(ax, 8, 80, y, -8, 8, labels=False, arrow_right=False)
for v, s in [(2, '2'), (3, '3'), (7.5, '7,5')]:
    disc(ax, f(v), y, 1.4, 'resultat')
    disc(ax, f(-v), y, 1.4, 'autre')
    text(ax, f(v), 23.5, s, 'resultat', 's')
    text(ax, f(-v), 23.5, '−' + s, 'autre', 's')
    arrow(ax, (f(v), y + 1.8), (f(-v), y + 1.8), 'varie', curve=0.5)
text(ax, f(0), 23.5, '0', 'fixe', 's')
brace(ax, f(0.8), f(8), 19, 'resultat', label='P')
brace(ax, f(-8), f(-0.8), 19, 'autre', label='N')
text(ax, 44, 52, 'chaque a de P donne −a', 'varie', 'm')
save(fig, '69-022')
