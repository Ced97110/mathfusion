import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc, Wedge, Rectangle
def rtri(ax,x,y,w,h,ca='varie',cb='sujet',cc='resultat',lw=1.4,da=False,db=False,r=None):
    A=(x,y);C=(x+w,y);B=(x+w,y+h)
    poly(ax,[A,C,B],'fixe',lw=0.1)
    line(ax,[A,C],cb,lw=lw,dash=db); line(ax,[C,B],ca,lw=lw,dash=da); line(ax,[A,B],cc,lw=lw)
    s=min(w,h)*0.14; line(ax,[(x+w-s,y),(x+w-s,y+s),(x+w,y+s)],'encre',lw=0.6)
    r=r or min(w,h)*0.22
    ax.add_patch(Arc(A,2*r,2*r,theta1=0,theta2=math.degrees(math.atan2(h,w)),color=COL['encre'],lw=0.8,zorder=3))
    return A,B,C
def hyp_off(A,B,d):
    mx,my=(A[0]+B[0])/2,(A[1]+B[1])/2; L=math.hypot(B[0]-A[0],B[1]-A[1])
    return (mx-(B[1]-A[1])/L*d, my+(B[0]-A[0])/L*d)

fig,ax=canvas(60)
x0,y0,w,h=8,14,44,33
A=(x0,y0);C=(x0+w,y0);B=(x0+w,y0+h)
poly(ax,[A,C,B],'fixe',lw=0.1)
ax.add_patch(Wedge(A,10,0,math.degrees(math.atan2(h,w)),ec=COL['sujet'],fc=FILL['sujet'],lw=1.0,zorder=2.5))
ax.add_patch(Wedge(B,8,180+math.degrees(math.atan2(h,w)),270,ec=COL['fixe'],fc=FILL['fixe'],lw=0.8,zorder=2.5))
line(ax,[A,C],'fixe',lw=1.4); line(ax,[C,B],'varie',lw=2.2); line(ax,[A,B],'fixe',lw=1.4)
line(ax,[A,(C[0],y0+h/2)],'varie',lw=1.0,dash=True)
arrow(ax,(C[0]-1.5,y0+h/2-0.5),(C[0]-0.2,y0+h/2-0.1),'varie',lw=1.0)
s_=3.2; line(ax,[(C[0]-s_,y0),(C[0]-s_,y0+s_),(C[0],y0+s_)],'encre',lw=0.6)
text(ax,A[0]+14,A[1]+6.5,'A','sujet','l',weight='bold')
text(ax,C[0]+2,y0+h/2,'3\nface à A','varie','m',ha='left')
text(ax,32,y0-3.5,'4','fixe','m')
p=hyp_off(A,B,4); text(ax,p[0],p[1],'5','fixe','m')
text(ax,A[0]+16,y0-9,'angle choisi','sujet','m'); arrow(ax,(A[0]+12,y0-6.2),(A[0]+8.5,y0+1.2),'sujet')
text(ax,B[0]-16,B[1]+3,'autre angle aigu','fixe','s'); arrow(ax,(B[0]-8,B[1]+1),(B[0]-2.5,B[1]-4),'fixe')
save(fig,'26-015')
