import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
f=numberline(ax,24,70,22,0,5)
for v in range(5):
    arrow(ax,(f(v)+0.5,24.2),(f(v+1)-0.5,24.2),'varie',curve=-0.6)
text(ax,50,32,'chaque flèche : +1','varie','s')
# the inverse (-1) would have to send 0 to a number below 0 : it does not exist
arrow(ax,(f(0)-2.5,22),(4,22),'limite',lw=1.2); ax.patches[-1].set_linestyle('--')
text(ax,13,26.5,r'$-1$','limite','m')
text(ax,13,16,'sans inverse','limite','s')
box(ax,2,40,44,9,'limite',label="0 : aucune flèche n'arrive",size='s')
arrow(ax,(f(0),40),(f(0),25.5),'limite')
text(ax,44,55,r'effet du nombre 1 : $n \mapsto n+1$','sujet','m')
text(ax,44,5,'sans inverse : pas de bijection','limite','m',weight='bold')
save(fig,'49-107')
