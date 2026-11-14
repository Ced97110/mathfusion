import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,8,76,34,-20,0,step=5,arrow_right=False)
disc(ax,f(-11),34,1.8,'varie'); disc(ax,f(-19),34,1.8,'limite')
text(ax,f(-11),47,'candidat −11','varie','s'); text(ax,f(-19),47,'radicande −19','limite','s')
arrow(ax,(f(-11)-2.5,38),(f(-19)+2.5,38),'varie')
text(ax,(f(-11)+f(-19))/2+2,41.5,r'$2\times(-11)+3$','varie','s')
box(ax,14,5,60,10,'resultat',label='aucune solution réelle')
save(fig,'22-141')
