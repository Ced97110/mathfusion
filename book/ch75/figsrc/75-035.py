import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 7
oy = 14
# left : e and trial arrow y = (0,3) -> area 3
x0 = 10
poly(ax, [(x0, oy), (x0+u, oy), (x0+u, oy+3*u), (x0, oy+3*u)], 'varie')
arrow(ax, (x0, oy), (x0+u, oy), 'sujet', lw=1.3); arrow(ax, (x0, oy), (x0, oy+3*u), 'varie', lw=1.3)
text(ax, x0+u/2+0.0, oy+1.5*u, '3', 'varie', 'l')
text(ax, x0+u+3, oy-3, r'$e_i$', 'sujet'); text(ax, x0-3.5, oy+3*u+1, r'$y$', 'varie')
text(ax, 15, 50, r'$B(e_i, y) = 3$', 'varie', 's')
# arrow division
arrow(ax, (30, oy+10), (48, oy+10), 'fixe', lw=1.0)
text(ax, 39, oy+14, r'$\div\ 3$', 'fixe', 'm')
# right : e and f = y/3 -> area 1
x1 = 58
poly(ax, [(x1, oy), (x1+u, oy), (x1+u, oy+u), (x1, oy+u)], 'resultat')
arrow(ax, (x1, oy), (x1+u, oy), 'sujet', lw=1.3); arrow(ax, (x1, oy), (x1, oy+u), 'resultat', lw=1.3)
text(ax, x1+u/2, oy+u/2, '1', 'resultat', 'l')
text(ax, x1+u+3, oy-3, r'$e_i$', 'sujet'); text(ax, x1-3.5, oy+u+1, r'$f_i$', 'resultat')
text(ax, 66, 50, r'$B(e_i, f_i) = 1$', 'resultat', 's')
save(fig, '75-035')
