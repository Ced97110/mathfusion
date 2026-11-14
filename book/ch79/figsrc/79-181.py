import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
N = {'60':(44,78),'12':(24,60),'30':(64,60),'6':(44,42),'2':(44,26),'1':(44,10)}
for a,b,r in [('60','12','sujet'),('12','6','sujet'),('60','30','varie'),('30','6','varie'),('6','2','fixe'),('2','1','fixe')]:
    line(ax, [N[a], N[b]], r, lw=1.8)
for k,(x,y) in N.items():
    disc(ax, x, y, 4.5, {'60':'fixe','1':'fixe','12':'sujet','30':'varie','6':'resultat','2':'fixe'}[k], label=k)
text(ax, 56, 80, r'$a$', 'fixe', 'm'); text(ax, 56, 10, r'$b$', 'fixe', 'm')
text(ax, 13, 60, r'$a_2$', 'sujet', 'm'); text(ax, 75, 60, r"$a'_2$", 'varie', 'm')
text(ax, 68, 42, r"$a_2\wedge a'_2$", 'resultat', 's')
text(ax, 70, 20, 'récurrence', 'fixe', 's'); 
text(ax, 20, 80, 'losange', 'resultat', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-181')
