import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
y=26
f=numberline(ax,10,76,y,0,6,labels=False,arrow_right=False)
line(ax,[(f(0),y),(f(5),y)],'resultat',lw=2.4)
for v in range(6): text(ax,f(v),y-4,str(v),'limite' if v==5 else 'encre','s')
for v in (0,1,2,4): disc(ax,f(v),y,1.5,'resultat')
disc(ax,f(3),y,2.0,'sujet'); disc(ax,f(5),y,1.8,'limite',fill=False,lw=1.2)
text(ax,f(3)-4,33,'$r=3$ pour 23 et 5','sujet','s'); text(ax,f(5)+3,33,'jamais 5','limite','s')
brace(ax,f(0),f(4),17,'resultat',label=r'$0\leq r<5$')
text(ax,44,50,'valeurs possibles de $r$','encre','m')
text(ax,44,6,'5 ferait un tas de plus','limite','s')
save(fig,'05-030')
