import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(ax, x, y, full, role="sujet", r=1.5):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else "white", lw=0.9, zorder=4))
def seg(ax, x0, x1, y, role="sujet", lw=2.6):
    ax.plot([x0, x1], [y, y], color=COL[role], lw=lw, zorder=3, solid_capstyle="butt")
def chev(ax, x, y, left=True, role="encre"):
    d = 1.0 if left else -1.0
    line(ax, [(x + d * 0.9, y + 1.3), (x - d * 0.9, y), (x + d * 0.9, y - 1.3)], role, lw=1.0)

fig, ax = canvas(88)
ys = [80, 50, 20]
for y, t, role in zip(ys, [r'$-4x+1<9$', r'$-4x<8$', r'$x>-2$'], ['sujet', 'sujet', 'resultat']):
    box(ax, 24, y - 6, 40, 12, role, label=t, size='m')
for (ya, yb), lab, note in zip([(73, 57), (43, 27)], [r'$-1$ des deux côtés', r'$\div(-4)$'], ['symbole inchangé', 'symbole retourné']):
    arrow(ax, (44, ya), (44, yb), 'varie')
    text(ax, 68, (ya + yb) / 2 + 3, lab, 'varie', 's', ha='center'); text(ax, 68, (ya + yb) / 2 - 3, note, 'varie', 's')
text(ax, 22, 6, r'$x=0$ : $1<9$ vrai', 'resultat', 's'); text(ax, 66, 6, r'$x=-3$ : $13<9$ faux', 'limite', 's')
save(fig, '17-090')
