import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 22; O = (14, 8); s3 = math.sqrt(3)/2
P = lambda a, b: (O[0]+(a+b*0.5)*u, O[1]+b*s3*u)
for b in range(0, 3):
    for a in range(-1, 4):
        p = P(a, b)
        if 3 < p[0] < 70 and (a, b) != (0, 0): disc(ax, p[0], p[1], 1.0, 'fixe')
q = (O[0], O[1]+u)
arrow(ax, O, (O[0]+u-1.5, O[1]), 'sujet', lw=1.3)
arrow(ax, O, (q[0], q[1]-1.8), 'limite', lw=1.0)
disc(ax, q[0], q[1], 1.6, 'limite', fill=False)
disc(ax, P(1, 0)[0], P(1, 0)[1], 1.5, 'sujet')
disc(ax, P(0, 1)[0], P(0, 1)[1], 1.5, 'resultat')
disc(ax, O[0], O[1], 1.1, 'encre')
text(ax, P(1, 0)[0]-3, O[1]-3.5, r'$x$', 'sujet', 'm')
text(ax, P(0, 1)[0]+4, P(0, 1)[1]-3, r'$y$', 'resultat', 'm')
text(ax, q[0]-8, q[1]+4, r'$(0,\,1)$', 'limite', 's')
text(ax, q[0]+12, q[1]+4.5, 'hors réseau', 'limite', 's')
text(ax, O[0]-3.5, O[1]-3.5, r'$O$', 'encre', 's')
text(ax, 74, 56, 'quart de tour : non', 'limite', 's')
text(ax, 74, 50, 'sixième : oui', 'resultat', 's')
text(ax, 74, 14, 'ordres 1, 2, 3, 6', 'sujet', 's')
save(fig, '74-140')
