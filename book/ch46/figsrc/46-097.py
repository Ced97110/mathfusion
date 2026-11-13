import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(92)
R=13; cy=60
for cx,step,role,title in [(22,4,'sujet',r'$o(4)=3$'),(66,5,'autre',r'$o(5)=12$')]:
    vis=[(step*i)%12 for i in range(12)]
    for k in range(12):
        p=cp(cx,cy,R,12,k); v=k in vis
        disc(ax,p[0],p[1],1.5 if v else 0.8,role if v else 'fixe')
    seq=[0]
    while True:
        nx=(seq[-1]+step)%12; seq.append(nx)
        if nx==0: break
    for a,b in zip(seq,seq[1:]):
        p,q=sh(cp(cx,cy,R,12,a),cp(cx,cy,R,12,b),2.0); arrow(ax,p,q,'varie',lw=0.7,curve=0.15)
    text(ax,cx,86,title,role,'l')
    text(ax,cx,cy-R-6,f'{len(seq)-1} pas','varie','m')
for cx,labs in [(22,[0,4,8]),(66,[0])]:
    for k in labs:
        p=cp(cx,cy,R+4,12,k); text(ax,p[0],p[1],str(k),'encre','s')
f=numberline(ax,8,60,18,0,6,labels=False,arrow_right=True)
for v in range(1,7): disc(ax,f(v),18,1.3,'varie')
disc(ax,f(0),18,1.5,'fixe'); text(ax,f(0),12,'0','encre','s')
text(ax,72,18,'jamais 0','limite','s')
text(ax,44,5,r'dans $\mathbb{Z}$ : $o(1)=\infty$','sujet','m')
save(fig,'46-097')
