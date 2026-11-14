import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=3.5))
    if label is not None: text(ax, x, y, label, role, size)
fig, ax = canvas(52)
y = 30
f = numberline(ax, 6, 80, y, -4, 13, labels=False, arrow_right=False, tick=0.8)
for v, role, lab in [(-3, 'sujet', '−3'), (-2, 'autre', '−2'), (2, 'autre', '2'), (3, 'sujet', '3'), (8, 'autre', '8'), (12, 'sujet', '12')]:
    disc(ax, f(v), y, 2, role, label=lab, size='s')
arrow(ax, (f(3), y + 2.2), (f(12), y + 2.2), 'sujet', curve=-0.35)
arrow(ax, (f(2), y + 2.2), (f(8), y + 2.2), 'autre', curve=-0.35)
arrow(ax, (f(3), y - 2.2), (f(-3), y - 2.2), 'sujet', curve=-0.35)
arrow(ax, (f(2), y - 2.2), (f(-2), y - 2.2), 'autre', curve=-0.35)
text(ax, 62, 45, '× 4 : sens gardé', 'resultat', 'm')
text(ax, 24, 14, '× (−1) : sens retourné', 'varie', 'm')
save(fig, '69-028')
