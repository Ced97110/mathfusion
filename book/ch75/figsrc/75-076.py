import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
u = 7
for oy, vs, role, lab, aire, nm in [(62, [(0,0),(3,1),(4,3),(1,2)], 'sujet', 'avant', r'$B(x,y)=5$', ('x','y')),
                          (14, [(0,0),(5,1),(10,3),(5,2)], 'resultat', 'après', r'$B(\tau x,\tau y)=5$', (r'$\tau x$', r'$\tau y$'))]:
    ox = 8
    P = lambda x, y, oy=oy: (ox + x * u, oy + y * u)
    poly(ax, [P(*p) for p in vs], role)
    arrow(ax, P(0,0), P(*vs[1]), role, lw=1.2); arrow(ax, P(0,0), P(*vs[3]), role, lw=1.2)
    nx = nm[0] if nm[0][0] == r'$' else r'$x$'; ny = nm[1] if nm[1][0] == r'$' else r'$y$'
    text(ax, P(*vs[1])[0] + 4, P(*vs[1])[1] - 3, nx, role, 's'); text(ax, P(*vs[3])[0] - 4, P(*vs[3])[1] + 3, ny, role, 's')
    text(ax, 4, oy + 28, lab, role, 's', ha='left') if False else text(ax, 70 if oy == 62 else 76, oy + 22 if oy == 62 else oy + 24, aire, role, 's')
arrow(ax, (44, 56), (44, 44), 'varie'); text(ax, 56, 50, r'$\tau_{u,c}$', 'varie', 's')
text(ax, 20, 93, 'avant', 'sujet', 's'); text(ax, 20, 45, 'après', 'resultat', 's')
text(ax, 44, 4, 'même aire', 'resultat', 'm')
save(fig, '75-076')
