import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(72)
for y, full, role, cap, note in ((48, False, 'limite', r'$n<8$ : strictement', 'refusé'), (16, True, 'resultat', r'$n\leq 8$ : au plus', 'permis')):
    f = numberline(ax, 8, 74, y, 5, 9, arrow_right=False)
    arrow(ax, (f(8), y), (8, y), 'sujet', lw=2.0)
    dot(ax, f(8), y, 'sujet', full=full, r=2.1)
    text(ax, f(8), y + 8, note, role, 's'); line(ax, [(f(8), y + 5.5), (f(8), y + 3.4)], role)
    text(ax, 4, y + 16, cap, 'sujet', 'm', ha='left')
save(fig, '17-036')
