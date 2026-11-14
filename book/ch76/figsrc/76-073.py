import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'$Le_1\wedge Le_2$ = nombre $\times\,e_{12}$', 'encre', 'm')
text(ax, 44, 51, r'gris : $e_{12}$ ; orange : image par $L$', 'fixe', 's')
u = 4.5
def sq(o): return [o, (o[0]+u, o[1]), (o[0]+u, o[1]+u), (o[0], o[1]+u)]
cases = [(4, 'première', [(2,1),(1,3)], '5'), (34, 'deuxième', [(2,0),(0,1)], '2'), (62, 'troisième', [(3,0),(0,3)], '9')]
for x, nm, (v1, v2), fac in cases:
    o = (x + 1, 12)
    P = [o, (o[0]+v1[0]*u, o[1]+v1[1]*u), (o[0]+(v1[0]+v2[0])*u, o[1]+(v1[1]+v2[1])*u), (o[0]+v2[0]*u, o[1]+v2[1]*u)]
    poly(ax, P, 'varie'); poly(ax, sq(o), 'fixe')
    t1 = (o[0]+v1[0]*u, o[1]+v1[1]*u); t2 = (o[0]+v2[0]*u, o[1]+v2[1]*u)
    arrow(ax, o, t1, 'varie', lw=1.2); arrow(ax, o, t2, 'varie', lw=1.2)
    text(ax, t1[0] + 5, t1[1] - 1.5, r'$Le_1$', 'varie', 's'); text(ax, t2[0] + 1, t2[1] + 3.5, r'$Le_2$', 'varie', 's')
    text(ax, x + 12, 5, rf'${fac}\,e_{{12}}$', 'varie', 'm')
    text(ax, x + 12, 44, nm, 'encre', 's')
save(fig, '76-073')
