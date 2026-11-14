import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 22; O = (24, 14)
s3 = math.sqrt(3)/2
P = lambda a, b: (O[0] + (a + b*0.5)*u, O[1] + b*s3*u)
for a in range(-1, 3):
    for b in range(0, 3):
        p = P(a, b)
        if 2 < p[0] < 60: disc(ax, p[0], p[1], 0.9, 'fixe')
arrow(ax, O, P(1, 0), 'sujet', lw=1.3)
arrow(ax, O, P(0, 1), 'autre', lw=1.3)
arrow(ax, O, P(-1, 1), 'resultat', lw=1.3)
arrow(ax, (O[0]+0.55*u, O[1]+0.05*u), (O[0]+0.3*u, O[1]+0.45*u), 'varie', curve=-0.3)
text(ax, P(1, 0)[0]+3.5, O[1]-0.5, r'$x$', 'sujet', 'l')
text(ax, P(0, 1)[0]+3.5, P(0, 1)[1]+2, r'$y$', 'autre', 'l')
text(ax, P(-1, 1)[0]-8, P(-1, 1)[1]+2.5, r'$y-x$', 'resultat', 'l')
text(ax, O[0]-3, O[1]-3, r'$O$', 'encre', 's')
text(ax, 72, 52, 'rotation de 60°', 'varie', 's')
text(ax, 72, 41, r'$M=\left(0\ -1\ ;\ 1\ \ 1\right)$', 'sujet', 's')
text(ax, 72, 31, r'trace $=1$', 'sujet', 's')
text(ax, 72, 23, r'$=2\cos 60^\circ$', 'resultat', 's')
save(fig, '74-130')
