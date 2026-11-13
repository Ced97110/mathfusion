import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
o1 = (6, 10); s = 10
poly(ax, [o1, (o1[0]+s, o1[1]), (o1[0]+s, o1[1]+s), (o1[0], o1[1]+s)], 'sujet')
arrow(ax, o1, (o1[0]+s, o1[1]), 'sujet'); arrow(ax, o1, (o1[0], o1[1]+s), 'autre')
text(ax, o1[0]+s+3.5, o1[1]-0.5, '$e_1$', 'sujet', 's'); text(ax, o1[0]-0.5, o1[1]+s+3, '$e_2$', 'autre', 's')
text(ax, 12, 4, r'$e_1\wedge e_2$', 'sujet', 's')
o2 = (46, 8); k = 11
P = [o2, (o2[0]+2*k, o2[1]+1*k), (o2[0]+3*k, o2[1]+4*k), (o2[0]+1*k, o2[1]+3*k)]
poly(ax, P, 'varie')
arrow(ax, o2, P[1], 'sujet'); arrow(ax, o2, P[3], 'autre')
text(ax, P[1][0]+5, P[1][1]-1, r'$Le_1$', 'sujet', 's'); text(ax, P[3][0]-6, P[3][1]+1, r'$Le_2$', 'autre', 's')
text(ax, 62.5, 29, r'$Le_1\wedge Le_2$', 'varie', 's')
arrow(ax, (24, 24), (42, 24), 'varie'); text(ax, 33, 28, r'$\eta(L)$', 'varie', 's')
save(fig, '76-072')
