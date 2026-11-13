import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'si $a\vee b$ recouvre $a$ et $b$', 'sujet', 's')
text(ax, 44, 74, r'alors $a$ et $b$ recouvrent $a\wedge b$', 'resultat', 's')
N = {'4':(44,14),'12':(22,35),'20':(66,35),'60':(44,56)}
for a,b in [('12','60'),('20','60')]: line(ax, [N[a], N[b]], 'sujet', lw=1.6)
for a,b in [('4','12'),('4','20')]: line(ax, [N[a], N[b]], 'resultat', lw=1.6)
for (x, y, l) in [(27,21,r'$\times3$'),(61,21,r'$\times5$'),(27,49,r'$\times5$'),(61,49,r'$\times3$')]:
    text(ax, x, y, l, 'fixe', 's')
for k,(x,y) in N.items():
    disc(ax, x, y, 5, {'4':'resultat','60':'sujet','12':'fixe','20':'fixe'}[k], label=k)
text(ax, 44, 65, r'$a\vee b = 60$', 'sujet', 's'); text(ax, 44, 5, r'$a\wedge b = 4$', 'resultat', 's')
text(ax, 8, 35, r'$a$', 'encre', 'm'); text(ax, 80, 35, r'$b$', 'encre', 'm')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-179')
