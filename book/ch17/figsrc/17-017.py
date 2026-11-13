import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = lambda v: 22 + v / 7 * 50
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=0.9, zorder=4))
rows = [(62, 'droite', '0 bout'), (38, 'segment', '2 bouts'), (14, 'demi-droite', '1 bout')]
for y, nom, n in rows:
    line(ax, [(22, y), (72, y)], 'fixe', lw=0.6)
    text(ax, 2, y, nom, 'encre', 's', ha='left')
    text(ax, 86, y, n, 'encre', 's', ha='right')
arrow(ax, (22, 62), (72, 62), 'autre', lw=2.2, both=True)
line(ax, [(f(2), 38), (f(5), 38)], 'autre', lw=2.2)
for v in (2, 5):
    dot(f(v), 38, 'autre'); text(ax, f(v), 31.5, str(v), 'autre', 's')
arrow(ax, (f(2), 14), (72, 14), 'sujet', lw=2.2)
dot(f(2), 14, 'sujet'); text(ax, f(2), 7.5, '2', 'sujet', 's')
save(fig, '17-017')
