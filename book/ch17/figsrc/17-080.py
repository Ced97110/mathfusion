import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70); y=22
f=numberline(ax,10,78,y,-1,8,labels=False,arrow_right=False)
line(ax,[(f(0),y),(f(6),y)],'resultat',lw=3)
disc(ax,f(0),y,2.4,'resultat',label='$0$',size='s'); disc(ax,f(6),y,2.4,'resultat',label='$6$',size='s')
box(ax,6,56,36,9,'varie',label=r'$15-3=12$',size='s'); box(ax,46,56,36,9,'varie',label=r'$12\div 2=6$',size='s')
arrow(ax,(42,60.5),(46,60.5),'varie')
arrow(ax,(f(6),55),(f(6),y+4),'varie')
text(ax,f(0),y-8,r'$d\geq 0$','sujet','s'); text(ax,f(6),y-8,r'$3+2d\leq 15$','sujet','s')
text(ax,44,y+18,r'$0\leq d\leq 6$','resultat','l')
for pt in ax.patches:
    if pt.__class__.__name__=='Circle': pt.set_zorder(3.5)
save(fig,'17-080')
