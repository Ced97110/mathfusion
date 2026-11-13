import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,r'$b\neq 0$','sujet','l')
y=48
f=numberline(ax,14,70,y,-2,2,labels=False,arrow_right=False)
for v,lab in ((-2,r'$-2$'),(-1,r'$-1$'),(0,'0'),(1,'1'),(2,'2')):
    text(ax,f(v),y-4,lab,'encre','s')
    if v!=0: disc(ax,f(v),y,1.6,'resultat')
disc(ax,f(0),y,1.8,'limite')
line(ax,[(f(0)-1.6,y-1.6),(f(0)+1.6,y+1.6)],'limite',lw=1.2); line(ax,[(f(0)-1.6,y+1.6),(f(0)+1.6,y-1.6)],'limite',lw=1.2)
text(ax,f(0),54,'interdit','limite','s'); text(ax,67,54,'tous les autres : permis','resultat','s')
for x in (8,34,60): box(ax,x,22,18,10,'sujet',label='23')
arrow(ax,(26,27),(34,27),'varie'); arrow(ax,(52,27),(60,27),'varie')
text(ax,44,12,'retirer 0 : 23 ne baisse pas','limite','m')
save(fig,'05-026')
