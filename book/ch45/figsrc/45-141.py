import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
xs=[14,34,54,74]
box(ax,2,14,84,30,'resultat',fill=False,dash=True,r=2)
text(ax,44,50,'centre = groupe entier','resultat','m',weight='bold')
for i,x in enumerate(xs): disc(ax,x,36,5,'sujet' if i==2 else 'fixe',label=str(i))
for i in (0,1,3):
    arrow(ax,(xs[2],31),(xs[i],31),'varie',both=True,curve=(-0.3 if i<2 else 0.3))
text(ax,44,8,r'$2+x=x+2$ pour chaque $x$','varie','s')
save(fig,'45-141')
