import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(96)
ys = [88, 62, 36, 10]
exs = [r'$-8x+5<14$', r'$5<14+8x$', r'$-9<8x$', r'$-\frac{9}{8}<x$']
for y, t, role in zip(ys, exs, ['autre', 'autre', 'autre', 'resultat']):
    box(ax, 22, y - 6, 40, 12, role, label=t, size='m')
for ya, lab in zip(ys[:3], [r'$+8x$ aux deux côtés', r'$-14$', r'$\div 8$ (positif)']):
    arrow(ax, (42, ya - 7), (42, ya - 19), 'varie')
    text(ax, 64, ya - 13, lab, 'varie', 's', ha='left')
save(fig, '17-095')
