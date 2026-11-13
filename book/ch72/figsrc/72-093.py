import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (14, 14); s = 28
arrow(ax, (o[0]-6, o[1]), (o[0]+62, o[1]), 'fixe', lw=0.6)
line(ax, [(o[0], o[1]-4), (o[0], o[1]+46)], 'fixe', lw=0.6)
m = (o[0]+s/2, o[1]+s/2); P = (o[0]+s, o[1])
arrow(ax, o, m, 'sujet', lw=1.8)
arrow(ax, m, P, 'autre', lw=1.8)
disc(ax, P[0], P[1], 1.5, 'resultat')
text(ax, m[0]-2, m[1]+1, r'$\frac{1}{2}u$', 'sujet', 'l', ha='right')
text(ax, (m[0]+P[0])/2+4, (m[1]+P[1])/2+4, r'$v$', 'autre', 'l', ha='left')
text(ax, P[0]+3, P[1]-5, r'$P=(1\ ;\ 0)$', 'resultat', 'm', ha='left')
text(ax, 44, 55, r'$P=\frac{1}{2}u+v$', 'resultat', 'l')
save(fig, '72-093')
