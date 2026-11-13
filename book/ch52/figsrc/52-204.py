import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
import math
cx,cy,R=22,34,14
P=[(cx+R*math.sin(2*math.pi*i/6),cy+R*math.cos(2*math.pi*i/6)) for i in range(6)]
for i in range(6):
    a,b=P[i],P[(i+1)%6]; d=math.hypot(b[0]-a[0],b[1]-a[1]); ux,uy=(b[0]-a[0])/d,(b[1]-a[1])/d
    arrow(ax,(a[0]+ux*4.2,a[1]+uy*4.2),(b[0]-ux*4.2,b[1]-uy*4.2),'varie')
for i,p in enumerate(P): disc(ax,p[0],p[1],3.6,'resultat' if i==0 else 'sujet',label=str(i),size='s')
text(ax,22,10,r'ℤ/6ℤ : 6 fois 1 donne 0','sujet','s')
text(ax,22,58,r'$k=6$','sujet','l')
q=[(56,44,'(0,0)'),(80,44,'(1,1)'),(56,24,'(1,0)'),(80,24,'(0,1)')]
for x,y,l in q: box(ax,x-8,y-4,16,8,'autre' if l in('(0,0)','(1,1)') else 'fixe',label=l,size='s')
arrow(ax,(58,49),(78,49),'varie',curve=-0.4); arrow(ax,(78,39),(58,39),'varie',curve=-0.4)
text(ax,68,58,r'$k=2$','autre','l')
text(ax,68,10,'4 éléments, k = 2','autre','s')
save(fig,'52-204')
