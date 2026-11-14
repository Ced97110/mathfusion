import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
N = {'1':(30,10),'2':(30,26),'4':(30,42),'12':(30,58),'20':(62,58),'60':(46,74)}
for a,b,r in [('1','2','sujet'),('2','4','sujet'),('4','12','sujet'),('4','20','fixe'),('12','60','fixe'),('20','60','fixe')]:
    line(ax, [N[a], N[b]], r, lw=1.8)
for k,(x,y) in N.items():
    disc(ax, x, y, 4.2, {'12':'resultat','20':'autre','60':'fixe'}.get(k,'sujet'), label=k)
for i in range(5):
    text(ax, 8, 10 + 16 * i, r'$d=%d$' % i, 'fixe', 's')
text(ax, 50, 34, '3 marches', 'sujet', 's')
text(ax, 75, 58, 'même rang 3', 'autre', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-185')
