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

fig,ax=canvas(72)
c=7.4; ytop=56
def grid(x0,title,trole,row,col,rl,cl,res,eq):
    text(ax,x0+2.5*c,ytop+5,title,trole,'m',weight='bold')
    for i in range(5):
        for j in range(5):
            role='fixe'
            if (i==row+1 and j>0) or (j==col+1 and i>0): role='varie'
            if i==row+1 and j==col+1: role='resultat'
            if i==0 and j==0: continue
            if i==0 and j!=col+1 or j==0 and i!=row+1: role='fixe'
            box(ax,x0+j*c,ytop-(i+1)*c,c,c,role,r=0.3,lw=0.6)
    text(ax,x0+(col+1.5)*c,ytop-0.5*c,cl,'varie','m',weight='bold')
    text(ax,x0+0.5*c,ytop-(row+1.5)*c,rl,'varie','m',weight='bold')
    text(ax,x0+(col+1.5)*c,ytop-(row+1.5)*c,res,'resultat','m',weight='bold')
    text(ax,x0+2.5*c,ytop-5*c-5,eq,trole,'s')
grid(3,'multiplication','fixe',2,3,'3','4','12',r'$3\times4=12$')
grid(47,r'horloge $\mathbb{Z}/4\mathbb{Z}$','sujet',3,2,'3','2','1',r'$3+2=5$, reste 1')
text(ax,44,5,r'ligne $x$, colonne $y$ : $x$ avec $y$','encre','m')
save(fig,'45-015')
