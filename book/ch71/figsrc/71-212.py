import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
o = (8, 10); u = 10
arrow(ax, (o[0], o[1]), (o[0]+5*u, o[1]), 'fixe', lw=0.7); arrow(ax, (o[0], o[1]), (o[0], o[1]+3.7*u), 'fixe', lw=0.7)
text(ax, o[0]+5*u, o[1]-2.5, r'$x$', 'fixe', 's'); text(ax, o[0]-2.5, o[1]+3.7*u, r'$y$', 'fixe', 's')
for k in range(3): arrow(ax, (o[0]+k*u, o[1]+k*u), (o[0]+(k+1)*u, o[1]+(k+1)*u), 'sujet', lw=1.3)
arrow(ax, (o[0]+3*u, o[1]+3*u), (o[0]+4*u, o[1]+2*u), 'varie', lw=1.3)
disc(ax, o[0]+4*u, o[1]+2*u, 1.1, 'resultat')
text(ax, o[0]+4*u+4, o[1]+2*u+3.5, r'$(4,\ 2)$', 'resultat', 's')
text(ax, o[0]+0.8*u, o[1]+2.4*u, r'3 fois $e_1$', 'sujet', 's', ha='right'); ax.texts[-1].set_x(o[0]+1.6*u)
text(ax, o[0]+3.9*u, o[1]+3.6*u, r'1 fois $e_2$', 'varie', 's')
text(ax, 72, 40, 'forme qui lit s', 'sujet', 's'); text(ax, 72, 34, r'$s=(x+y)/2=3$', 'sujet', 's')
text(ax, 72, 24, 'forme qui lit t', 'varie', 's'); text(ax, 72, 18, r'$t=(x-y)/2=1$', 'varie', 's')
save(fig, '71-212')
