import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,80,'départ : deux écritures de a','encre','s')
box(ax,8,64,72,11,'sujet',label=r'$b(q-q^{\prime})=r^{\prime}-r$',size='l')
arrow(ax,(30,64),(30,56.5),'varie')
text(ax,34,60.5,r'étape : $r^{\prime}-r=b\times$ entier','varie','s',ha='left')
y=42
f=numberline(ax,8,80,y,0,12,step=1,labels=False,arrow_right=False)
box(ax,f(0),y+3,f(4)-f(0),3.5,'resultat')
text(ax,8,y+10,r'écart $r^{\prime}-r$ : de 0 à 4','resultat','s',ha='left')
for v,r in [(0,'resultat'),(5,'limite'),(10,'limite')]:
    disc(ax,f(v),y,1.9,r)
    text(ax,f(v),y-4.5,str(v),r,'s')
text(ax,f(5),y-9,'5 : trop grand','limite','s')
text(ax,f(10)+3,y-14,r'multiples de $b$','varie','s')
arrow(ax,(f(0),y-6.5),(f(0),19),'resultat')
text(ax,f(0)+3,y-14,'seul 0 convient','resultat','s',ha='left')
box(ax,8,6,72,12,'resultat',label=r'$r^{\prime}=r$, puis $q^{\prime}=q$',size='l')
save(fig,'05-039')
