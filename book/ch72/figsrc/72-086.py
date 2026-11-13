import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (8, 12); s = 30
arrow(ax, (o[0], o[1]), (o[0]+50, o[1]), 'fixe', lw=0.6)
line(ax, [(o[0], o[1]), (o[0], o[1]+40)], 'fixe', lw=0.6)
P = (o[0]+s, o[1]); Q = (o[0]+1.25*s, o[1]+0.75*s)
arrow(ax, o, P, 'sujet', lw=1.4); arrow(ax, o, Q, 'resultat', lw=1.4)
arrow(ax, (P[0]+3, P[1]+3), (Q[0]-1, Q[1]-4), 'varie', lw=1.0, curve=-0.3)
text(ax, P[0], P[1]-4, r'$x=(1\ ;\ 0)$', 'sujet', 'm')
text(ax, Q[0]+3, Q[1]+3, r'$\eta x=(\frac{5}{4}\ ;\ \frac{3}{4})$', 'resultat', 'm', ha='left')
text(ax, P[0]+11, (P[1]+Q[1])/2-2, r'$\eta$', 'varie', 'xl')
text(ax, 44, 4.5, r'$B(\eta x,\eta y)=B(x,y)$', 'varie', 'm')
save(fig, '72-086')
