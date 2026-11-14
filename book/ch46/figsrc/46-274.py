import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'Nombre d’éléments $n!/2$','encre','m')
f=numberline(ax,14,70,28,1,4,arrow_right=False,size='m',tick=1.4)
text(ax,4,28,r'$n$','encre','m')
vals={1:('1/2','limite'),2:('1','resultat'),3:('3','resultat'),4:('12','resultat')}
for n,(v,r) in vals.items():
    disc(ax,f(n),28,3.2,r) if False else None
    box(ax,f(n)-6,8,12,9,r,label=v)
    arrow(ax,(f(n),24),(f(n),17.8),r)
text(ax,4,12.5,'','encre')
text(ax,f(1),38,'aucune transposition','limite','s')
text(ax,f(3.5),38,r'$n \geq 2$ : entier','resultat','s')
save(fig,'46-274')
