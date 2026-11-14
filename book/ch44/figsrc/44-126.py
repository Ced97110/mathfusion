import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 14
def sq(x, y, role, corner, axis=None):
    box(ax, x, y, s, s, role, r=0.5)
    cx = [x + 3, x + s - 3, x + s - 3, x + 3][corner]; cy = [y + s - 3, y + s - 3, y + 3, y + 3][corner]
    disc(ax, cx, cy, 1.5, 'varie')
    if axis is not None:
        pts = [((x + s / 2, y - 1.5), (x + s / 2, y + s + 1.5)), ((x - 1.5, y + s / 2), (x + s + 1.5, y + s / 2)),
               ((x - 1.5, y - 1.5), (x + s + 1.5, y + s + 1.5)), ((x - 1.5, y + s + 1.5), (x + s + 1.5, y - 1.5))][axis]
        line(ax, list(pts), 'varie', dash=True)
text(ax, 44, 74, r'$D_4$ : 8 éléments, sous-groupe de $S_4$', 'sujet', 's')
labs = ['1', r'$r$', r'$r^2$', r'$r^3$']
for i in range(4):
    x = 6 + i * 21
    sq(x, 44, 'sujet', i)
    text(ax, x + s / 2, 38, labs[i], 'sujet', 'm')
text(ax, 44, 64, '4 rotations (quarts de tour)', 'sujet', 's')
text(ax, 44, 30, '4 retournements (autour d\'un axe)', 'autre', 's')
for i in range(4):
    sq(6 + i * 21, 8, 'autre', i, axis=i)
save(fig, '44-126')
