import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cp(cx,cy,R,n,k):
    a=math.radians(90-360*k/n); return (cx+R*math.cos(a), cy+R*math.sin(a))
def sh(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d),(q[0]-dx/L*d,q[1]-dy/L*d)

fig,ax=canvas(70)
cx,cy,R=20,40,13
for k in range(12):
    p=cp(cx,cy,R,12,k); v=k%4==0
    disc(ax,p[0],p[1],1.6 if v else 0.8,'sujet' if v else 'fixe')
for a,b in [(0,4),(4,8),(8,0)]:
    p,q=sh(cp(cx,cy,R,12,a),cp(cx,cy,R,12,b),2.2); arrow(ax,p,q,'varie',lw=0.8,curve=0.15)
for k in (0,4,8):
    p=cp(cx,cy,R+4,12,k); text(ax,p[0],p[1],str(k),'encre','s')
text(ax,20,12,'horloge, $a=4$','fixe','s')
labs=['0','4','8','0','4','8']; sub=['$e$','$a$',r'$a^2$']
for i,l in enumerate(labs):
    x=44+i*7.2; role='sujet' if i<3 else 'limite'
    box(ax,x,34,6.4,8,role,label=l,size='s')
    if i<3: text(ax,x+3.2,29,sub[i],'sujet','s')
brace(ax,44,44+3*7.2-0.8,46,'sujet',label=r'$r=3$ distincts',down=False,size='s')
text(ax,44+4.5*7.2-0.4,52,'répétés','limite','s')
save(fig,'46-101')
