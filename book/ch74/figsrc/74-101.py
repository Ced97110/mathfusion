import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (14, 14); u = 12
for i in range(6):
    for j in range(4):
        disc(ax, o[0]+i*u, o[1]+j*u, 0.9, 'sujet')
arrow(ax, o, (o[0]+u-1.5, o[1]), 'varie', lw=1.4)
arrow(ax, o, (o[0], o[1]+u-1.5), 'varie', lw=1.4)
text(ax, o[0]+u/2, o[1]-3.5, r'$x$', 'varie', 'm')
text(ax, o[0]-3.5, o[1]+u/2, r'$y$', 'varie', 'm')
disc(ax, o[0]+3*u, o[1]+2*u, 2.2, 'resultat')
text(ax, o[0]+3*u+9, o[1]+2*u+4, r'$3x+2y$', 'resultat', 's')
disc(ax, o[0]+0.5*u, o[1], 1.5, 'limite', fill=False, lw=1.0)
text(ax, 50, 4, r'$0{,}5\,x$ : hors de $L$', 'limite', 's')
text(ax, 62, 58, r'$L$ : tous les points $mx+ny$', 'sujet', 's')
text(ax, 62, 53, r'$m,\ n$ entiers', 'sujet', 's')
save(fig, '74-101')
