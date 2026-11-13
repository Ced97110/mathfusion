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
c=7.4; ytop=56
EL=['sujet','varie','resultat','limite']
def table(x0,title,trole):
    text(ax,x0+2.5*c,ytop+5,title,trole,'m',weight='bold')
    for k in range(4):
        box(ax,x0+(k+1)*c,ytop-c,c,c,EL[k],r=0.3,lw=0.6)
        box(ax,x0,ytop-(k+2)*c,c,c,EL[k],r=0.3,lw=0.6)
    for i in range(4):
        for j in range(4):
            box(ax,x0+(j+1)*c,ytop-(i+2)*c,c,c,EL[(i+j)%4],r=0.3,lw=0.6)
    box(ax,x0+3*c,ytop-5*c,c,c,'encre',fill=False,lw=1.8,r=0.3)
table(2,r'$\mathbb{Z}/4\mathbb{Z}$','sujet')
table(49,'rotations','autre')
arrow(ax,(40,ytop-2.5*c),(48,ytop-2.5*c),'varie',lw=1.3)
text(ax,44,ytop-2.5*c+4,r'$\eta$','varie','l',weight='bold')
for k in range(4):
    x=2+k*21
    box(ax,x,3,5,5,EL[k],r=0.3,lw=0.6)
    text(ax,x+6.5,5.5,r'$%d\mapsto r_%d$'%(k,k),'encre','s',ha='left')
save(fig,'45-014')
