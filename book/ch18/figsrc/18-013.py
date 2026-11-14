import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,6,46,34,10,'sujet',label=r'$6x+9$'); box(ax,48,46,34,10,'autre',label=r'$3(2x+3)$')
text(ax,23,59,'forme somme','sujet','s'); text(ax,65,59,'forme produit','autre','s')
for i,(xv,v) in enumerate([(1,15),(5,39)]):
    y=28-i*16
    box(ax,6,y,34,9,'sujet',fill=False,label=str(v)); box(ax,48,y,34,9,'autre',fill=False,label=str(v))
    text(ax,44,y+4.5,'=','resultat','l',weight='bold')
    text(ax,44,y+12.5,f'$x={xv}$','encre','s')
save(fig,'18-013')
