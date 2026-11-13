import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
u=3.0; x0=4; xs=[x0,x0+5*u,x0+10*u,x0+16*u]
brace(ax,xs[0]+0.3,xs[3]-0.3,48,'encre',r'$Q(1,\,1)=16$',down=False)
for i,(role,lab) in enumerate([('sujet','5'),('autre','5'),('varie','6')]):
    box(ax,xs[i],38,xs[i+1]-xs[i],8,role,label=lab,r=0.3)
text(ax,(xs[0]+xs[1])/2,33.5,r'$Q(1,\,0)$','sujet','s'); text(ax,(xs[1]+xs[2])/2,33.5,r'$Q(0,\,1)$','autre','s'); text(ax,(xs[2]+xs[3])/2,33.5,'reste','varie','s')
m=(xs[2]+xs[3])/2
box(ax,xs[2],20,m-xs[2],8,'fixe',label='3',r=0.3); box(ax,m,20,xs[3]-m,8,'resultat',label='3',r=0.3)
text(ax,m,15,'moitié du reste','resultat','s')
for r,c,v,role in [(0,0,'5','fixe'),(0,1,'3','resultat'),(1,0,'3','resultat'),(1,1,'5','fixe')]:
    box(ax,62+c*12,34+(1-r)*10,12,10,role,label=v,size='m')
text(ax,74,58,'matrice','sujet','s')
arrow(ax,(xs[3],24),(62,39),'resultat',curve=0.2)
save(fig,'71-119')
