import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
x0,y0=26,50; cw=26; ch=12
text(ax,x0+cw/2,y0+2*ch+4,r'$2$','sujet','m'); text(ax,x0+1.5*cw,y0+2*ch+4,r'$3\sqrt{2}$','sujet','m')
text(ax,x0-5,y0+1.5*ch,r'$1$','sujet','m'); text(ax,x0-5,y0+0.5*ch,r'$\sqrt{2}$','sujet','m')
cells=[(0,1,r'$2$','sujet'),(1,1,r'$3\sqrt{2}$','autre'),(0,0,r'$2\sqrt{2}$','autre'),(1,0,r'$6$','sujet')]
for c,r,s,role in cells: box(ax,x0+c*cw,y0+r*ch,cw,ch,role,label=s,size='l')
text(ax,44,y0-5,r'$\sqrt{2}\times\sqrt{2}=2$ , donc $3\times 2=6$','varie','s')
arrow(ax,(65,y0-2.6),(65,y0-0.2),'varie')
text(ax,44,38,'on regroupe','fixe','s')
text(ax,24,28,r'$2+6=8$','sujet','l'); text(ax,64,28,r'$3+2=5$','autre','l')
text(ax,24,21,'entiers','sujet','s'); text(ax,64,21,r'multiples de $\sqrt{2}$','autre','s')
box(ax,16,4,56,11,'resultat',label=r'$8+5\sqrt{2}$',size='l')
save(fig,'51-070')
