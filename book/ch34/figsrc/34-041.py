import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,3,40,36,18,'varie',label=r'$rp\,\sin(A+B)$'+'\n'+r'$195\times\sin(A+B)$')
box(ax,49,40,36,18,'sujet',label=r'$xh+yh$'+'\n'+'168')
text(ax,44,49,'=','encre','xl')
arrow(ax,(21,40),(21,29),'varie');arrow(ax,(67,40),(67,29),'varie')
text(ax,21,34.5,r'$\div\,rp$','varie','s',ha='left') if False else None
text(ax,31,34.5,r'$\div195$','varie','s');text(ax,77,34.5,r'$\div195$','varie','s')
box(ax,3,17,36,11,'resultat',label=r'$\sin(A+B)$')
box(ax,49,17,36,11,'resultat',label=r'$\frac{168}{195}=\frac{56}{65}$')
text(ax,44,22.5,'=','resultat','xl')
text(ax,44,9,r'$r=13>0$ et $p=15>0$','encre','s')
text(ax,44,3.5,'donc 195 > 0 : division permise','encre','s')
save(fig,'34-041')
