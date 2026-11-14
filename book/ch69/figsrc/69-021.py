import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(56)
y = 26
f = numberline(ax, 8, 74, y, 0, 10, every=2, arrow_right=False)
box(ax, f(0), 38, f(10) - f(0), 8, 'resultat', label='P')
for v, role, lab in [(2, 'sujet', 'a = 2'), (4, 'autre', 'b = 4'), (6, 'resultat', 'a + b = 6'), (8, 'resultat', 'ab = 8')]:
    disc(ax, f(v), y, 1.8, role)
    text(ax, f(v), 32, lab, role, 's')
text(ax, 41, 51, 'a + b et ab restent dans P', 'resultat', 'm')
save(fig, '69-021')
