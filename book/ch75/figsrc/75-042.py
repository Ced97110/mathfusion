import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 3.2
def grid(ox, oy, nc, nr, role):
    for i in range(nc):
        for j in range(nr):
            box(ax, ox + i*s, oy + j*s, s, s, role, r=0.2, lw=0.5)
grid(5, 18, 2, 2, 'sujet'); grid(17, 18, 4, 2, 'autre')
text(ax, 8, 12, '4', 'sujet', 'l'); text(ax, 23, 12, '8', 'autre', 'l')
text(ax, 17, 38, 'orthogonal', 'encre', 'm'); text(ax, 17, 33, '2 familles', 'fixe', 's')
line(ax, [(41, 8), (41, 50)], 'fixe', dash=True)
grid(51, 18, 6, 4, 'resultat')
text(ax, 65, 12, '24', 'resultat', 'l')
text(ax, 65, 46, 'symplectique', 'encre', 'm'); text(ax, 65, 41, '1 famille', 'fixe', 's')
text(ax, 17, 48, 'éléments du groupe', 'fixe', 's')
save(fig, '75-042')
