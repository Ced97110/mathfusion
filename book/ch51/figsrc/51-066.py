import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[16,44,72]
for x,s in zip(xs,['ℤ','ℚ','ℝ']):
    box(ax,x-12,42,24,14,'sujet'); text(ax,x,49,s,'sujet','xl',weight='bold')
    text(ax,x,34,'8 règles : vraies','resultat','s')
    text(ax,x,22,'inverse de 2','fixe','s')
for x in xs[1:]: text(ax,x,12,r'$\frac{1}{2}$','resultat','l')
text(ax,xs[0],12,'aucun','limite','m',weight='bold')
save(fig,'51-066')
