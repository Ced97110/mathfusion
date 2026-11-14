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
cx,cy,R=26,33,12
disc(ax,cx,cy,R,'fixe',fill=False)
roles={0:'fixe',1:'resultat',2:'fixe',3:'sujet'}
for k in range(4):
    a=math.radians(90-90*k)
    disc(ax,cx+R*math.cos(a),cy+R*math.sin(a),4.6,roles[k],label=str(k),size='l')
arcarrow(ax,cx,cy,R+8.5,180,0)
text(ax,cx,cy+R+13.5,'+ 2','varie','m')
text(ax,67,52,'départ : 3','sujet','m')
text(ax,67,42,r'$3+2=5$ : pas de 5','limite','m')
text(ax,67,32,'reste de 5 ÷ 4 : 1','encre','m')
text(ax,67,22,'arrivée : 1','resultat','m',weight='bold')
save(fig,'45-001')
