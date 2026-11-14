import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sq(ax,cx,cy,s,k,role='sujet'):
    d=s*0.7071
    poly(ax,[(cx+d*math.cos(math.radians(45+90*j)),cy+d*math.sin(math.radians(45+90*j))) for j in range(4)],role)
    a=math.radians(45-90*k)
    disc(ax,cx+0.66*d*math.cos(a),cy+0.66*d*math.sin(a),s*0.1,'varie')
def clk(ax,cx,cy,r,k,role='sujet'):
    disc(ax,cx,cy,r,role)
    for j in range(4):
        a=math.radians(90-90*j); disc(ax,cx+0.78*r*math.cos(a),cy+0.78*r*math.sin(a),r*0.09,'fixe')
    a=math.radians(90-90*k); arrow(ax,(cx,cy),(cx+0.62*r*math.cos(a),cy+0.62*r*math.sin(a)),'varie',lw=1.1)
def arcarrow(ax,cx,cy,r,a0,a1,role='varie'):
    n=24; pts=[(cx+r*math.cos(math.radians(a0+(a1-a0)*i/n)),cy+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw=1.1); arrow(ax,pts[-2],pts[-1],role,lw=1.1)
def edge_arrow(ax,c1,c2,w,h,role='varie',curve=0.0,m=0.8):
    dx,dy=c2[0]-c1[0],c2[1]-c1[1]
    t=min((w/2+m)/abs(dx) if dx else 9e9,(h/2+m)/abs(dy) if dy else 9e9)
    arrow(ax,(c1[0]+t*dx,c1[1]+t*dy),(c2[0]-t*dx,c2[1]-t*dy),role,curve=curve)

fig,ax=canvas(74)
xs=[8+14*i for i in range(5)]; bw=11
for i,x in enumerate(xs):
    box(ax,x,52,bw,9,'sujet' if i<3 else 'varie',label='2',size='m')
    sq(ax,x+bw/2,30,9,1,'sujet' if i<3 else 'varie')
brace(ax,xs[0],xs[2]+bw,63,'sujet','3 facteurs',down=False)
brace(ax,xs[3],xs[4]+bw,63,'varie','2 facteurs',down=False)
brace(ax,xs[0],xs[2]+bw,37,'sujet','3 fois',down=False)
brace(ax,xs[3],xs[4]+bw,37,'varie','2 fois',down=False)
brace(ax,xs[0],xs[4]+bw,50,'resultat','5 facteurs',down=True)
brace(ax,xs[0],xs[4]+bw,22,'resultat','5 quarts de tour',down=True)
text(ax,44,6,'un quart de tour, répété','fixe','s')
save(fig,'45-010')
