import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cx,cy,R=30,36,20
lab=['a','a²','a³','1']
P=[(cx+R*math.cos(math.radians(90-90*i)),cy+R*math.sin(math.radians(90-90*i))) for i in range(4)]
for i,p in enumerate(P):
    disc(ax,p[0],p[1],4.5,'sujet' if i<3 else 'resultat',label=lab[i],size='m')
for i in range(4):
    a,b=P[i],P[(i+1)%4]
    d=math.hypot(b[0]-a[0],b[1]-a[1]); ux,uy=(b[0]-a[0])/d,(b[1]-a[1])/d
    arrow(ax,(a[0]+5.3*ux,a[1]+5.3*uy),(b[0]-5.3*ux,b[1]-5.3*uy),'varie',curve=-0.25)
text(ax,cx,cy,'× a','varie','m')
text(ax,66,56,'puissances de a','sujet','m')
text(ax,66,38,'a² · a³ = a⁵ = a','resultat','m')
text(ax,66,28,'encore une puissance','resultat','s')
text(ax,66,16,'a⁴ = 1 : tour entier','resultat','s')
save(fig,'45-247')
