import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
o = (44, 12); s = 10
arrow(ax, (o[0]-30, o[1]), (o[0]+36, o[1]), 'fixe', lw=0.6)
line(ax, [(o[0], o[1]-0), (o[0], o[1]+50)], 'fixe', lw=0.6)
arrow(ax, o, (o[0]+2*s, o[1]+1*s), 'sujet', lw=1.4)
arrow(ax, o, (o[0]-1*s, o[1]+2*s), 'autre', lw=1.4)
d1 = (2/5**.5, 1/5**.5); d2 = (-1/5**.5, 2/5**.5); k = 3
p1 = (o[0]+k*d1[0], o[1]+k*d1[1]); p3 = (o[0]+k*d2[0], o[1]+k*d2[1]); p2 = (p1[0]+k*d2[0], p1[1]+k*d2[1])
line(ax, [p1, p2, p3], 'resultat', lw=0.8)
text(ax, o[0]+2*s+2, o[1]+1*s-1, r'$x=(2\ ;\ 1)$', 'sujet', 'm', ha='left')
text(ax, o[0]-1*s-2, o[1]+2*s+3, r'$y=(-1\ ;\ 2)$', 'autre', 'm', ha='right')
text(ax, 44, 55, r'$x\perp y$', 'resultat', 'xl')
text(ax, 44, 4, r'$2\times(-1)+1\times 2=0$', 'resultat', 'm')
save(fig, '72-081')
