import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
N = {'60':(26,60),'12':(10,38),'20':(42,38),'4':(26,16)}
for a,b in [('4','12'),('4','20'),('12','60'),('20','60')]: line(ax, [N[a], N[b]], 'fixe', lw=1.2)
rk = {'60':4,'12':3,'20':3,'4':2}
off = {'60':(0,9),'12':(0,-8),'20':(0,-8),'4':(0,-9)}
for k,(x,y) in N.items():
    disc(ax, x, y, 4.5, {'60':'resultat','4':'resultat','12':'sujet','20':'autre'}[k], label=k)
    text(ax, x + off[k][0], y + off[k][1], r'$d=%d$' % rk[k], 'fixe', 's')
text(ax, 70, 68, 'sup et inf : 60, 4', 'resultat', 's')
text(ax, 70, 58, r'$4+2=6$', 'resultat', 'l', weight='bold')
text(ax, 70, 44, '=', 'encre', 'l')
text(ax, 70, 30, r'$3+3=6$', 'encre', 'l', weight='bold')
text(ax, 70, 20, 'rangs de 12 et 20', 'encre', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-186')
