import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
c=(44,46); R=18
labs=['colonnes\northonormées','inverse =\ntransposée','garde le\nproduit scalaire','garde la\ndistance','garde la\nlongueur']
angs=[90,18,-54,-126,162]
pts=[(c[0]+R*math.cos(math.radians(a)),c[1]+R*math.sin(math.radians(a))) for a in angs]
for i in range(5):
    a=math.radians(angs[i]); b=math.radians(angs[(i+1)%5])
    p=(c[0]+R*math.cos(a),c[1]+R*math.sin(a)); q=(c[0]+R*math.cos(b),c[1]+R*math.sin(b))
    d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d
    arrow(ax,(p[0]+4.2*ux,p[1]+4.2*uy),(q[0]-4.2*ux,q[1]-4.2*uy),'varie')
for i,(x,y) in enumerate(pts):
    disc(ax,x,y,3.6,'sujet',label=str(i+1),size='m')
off=[(0,9,'center'),(7,0,'left'),(5,-8,'left'),(-5,-8,'right'),(-7,0,'right')]
for i,(x,y) in enumerate(pts):
    dx,dy,ha=off[i]; text(ax,x+dx,y+dy,labs[i],'sujet','s',ha=ha)
text(ax,c[0],c[1],'une seule\npropriété','resultat','s')
save(fig,'73-232')
