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

fig,ax=canvas(68)
w,h=18,14
X=[16,38]; Y=[40,10]
ctr=lambda a,b:(X[b]+w/2,Y[a]+h/2)
for a in range(2):
    for b in range(2):
        vis=(a==b)
        box(ax,X[b],Y[a],w,h,'resultat' if vis else 'fixe',fill=vis,dash=not vis,label=('0 ou 2' if a==0 else '1') if vis else 'jamais',size='m' if vis else 's')
edge_arrow(ax,ctr(0,0),ctr(1,1),w,h,'varie',curve=0.25)
edge_arrow(ax,ctr(1,1),ctr(0,0),w,h,'varie',curve=0.25)
arrow(ax,(X[1]+3,Y[1]+h+0.5),(X[0]+w-3,Y[0]-0.5),'varie',curve=0.0) if False else None
text(ax,X[0]+w+11,57,'interrupteur 2','autre','s') if False else text(ax,X[0]+w+2,62,'interrupteur 2','autre','s')
for b in range(2): text(ax,X[b]+w/2,55,str(b),'autre','m')
text(ax,4,Y[1]+h,'interrupteur 1','sujet','s',rot=90)
for a in range(2): text(ax,11,Y[a]+h/2,str(a),'sujet','m')
text(ax,72,38,'4 états possibles','fixe','s')
text(ax,72,28,'2 états visités','resultat','s',weight='bold')
save(fig,'45-012')
