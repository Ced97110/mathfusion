import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
cx,cy,R=34,40,19
disc(ax,cx,cy,R,'fixe',fill=False)
line(ax,[(3,9),(81,9)],'fixe')
ang=[(0,'0','sujet'),(1,r'$\pi/2$','varie'),(2,r'$\pi$','fixe'),(3,r'$3\pi/2$','autre'),(4,r'$2\pi$','sujet'),(5,r'$5\pi/2$','varie')]
for k,lab,r in ang:
    x=8+14.5*k; disc(ax,x,9,2,r); text(ax,x,3.8,lab,r,'s')
for k,r,(dx,dy),ha,lab in [(0,'sujet',(3.5,0),'left',r'1 : $0$ et $2\pi$'),(1,'varie',(0,4.5),'center',r'$i$ : $\pi/2$ et $5\pi/2$'),(2,'fixe',(-3.5,0),'right',r'−1 : $\pi$'),(3,'autre',(0,-4.5),'center',r'$-i$ : $3\pi/2$')]:
    a=math.radians(90*k); x=cx+R*math.cos(a); y=cy+R*math.sin(a)
    disc(ax,x,y,2.2,r); text(ax,x+dx,y+dy,lab,r,'s',ha=ha)
text(ax,cx,cy,'un tour\npar 2π','fixe','s')
text(ax,44,69,'angles : une même couleur = un même point','encre','s')
save(fig,'48-151')
