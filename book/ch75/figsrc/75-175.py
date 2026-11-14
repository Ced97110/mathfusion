import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# row 1 : B takes two arrows and returns a number
ox, oy, u = 5, 62, 17
P = lambda x, y: (ox + x*u, oy + y*u)
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'varie')
arrow(ax, P(0, 0), P(1.25, 0), 'sujet', lw=1.3); arrow(ax, P(0, 0), P(0, 1.25), 'autre', lw=1.3)
text(ax, *P(.5, .5), 'aire 1', 'varie', 's', weight='bold')
text(ax, P(1.25, 0)[0] + 1, oy - 3, '$(1,0)$', 'sujet', 's', ha='left'); text(ax, ox + 8, P(0, 1.25)[1] + 4, '$(0,1)$', 'autre', 's')
line(ax, [(29, 78), (36, 78)], 'sujet', dash=True); line(ax, [(29, 70), (36, 70)], 'autre', dash=True)
arrow(ax, (36, 78), (43.5, 78), 'sujet'); arrow(ax, (36, 70), (43.5, 70), 'autre')
box(ax, 44, 64, 16, 20, 'sujet', label='$B$', size='l', weight='bold')
arrow(ax, (60.5, 74), (67, 74), 'varie')
box(ax, 68, 68, 16, 12, 'varie', label='1', size='l', weight='bold')
text(ax, 52, 88, 'deux flèches, un nombre', 'sujet', 's')
# row 2 : the determinant, and the volume in dimension 3
box(ax, 4, 22, 28, 20, 'varie')
for (tx, ty, t, r) in ((11, 36, '1', 'sujet'), (11, 28, '0', 'sujet'), (25, 36, '0', 'autre'), (25, 28, '1', 'autre')):
    text(ax, tx, ty, t, r, 'l', weight='bold')
text(ax, 18, 17, 'déterminant : 1', 'varie', 's', weight='bold')
cubes(ax, [(0, 0, 0)], (62, 20), 12, 'varie')
text(ax, 62, 10, 'dimension 3 : volume', 'fixe', 's'); text(ax, 62, 5, 'orienté', 'fixe', 's')
text(ax, 44, 50, 'aire et déterminant : même nombre', 'resultat', 's', weight='bold')
line(ax, [(2, 55), (86, 55)], 'fixe', dash=True)
save(fig, '75-175')
