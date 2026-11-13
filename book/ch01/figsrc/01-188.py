import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
X = lambda v: 44 + 9 * v
def dot(x, y, r, role):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role], lw=0.8, zorder=3.6))
line(ax, [(44, 46), (84, 46)], 'fixe')
for v in range(5):
    dot(X(v), 46, 1.3, 'fixe')
for v in range(4):
    text(ax, X(v), 41, str(v), 'fixe', 's')
    line(ax, [(X(v), 22), (X(v), 38.8)], 'fixe', dash=True)
line(ax, [(X(4), 22), (X(4), 44)], 'fixe', dash=True)
text(ax, 22, 46, 'entiers naturels', 'fixe', 's')
numberline(ax, 8, 80, 20, -4, 4, 1, labels=False, role='sujet')
for x, s in [(17, '−3'), (44, '0'), (53, '1'), (62, '2'), (71, '3')]:
    text(ax, x, 15, s, 'sujet', 's')
text(ax, 44, 6, 'droite des réels', 'sujet', 'm')
for x, s in [(66.5, '2,5'), (56.7, r'$\sqrt{2}$')]:
    dot(x, 20, 1.5, 'autre'); text(ax, x, 25, s, 'autre', 's')
dot(17, 20, 1.5, 'autre')
brace(ax, 8, 43, 23, 'autre', label='nombres négatifs', down=False)
save(fig, '01-188')
