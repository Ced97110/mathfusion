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

fig,ax=canvas(56)
u=3.6; A=(8,14)
Cb=(A[0]+12*u,A[1]); Bb=(Cb[0],A[1]+9*u)
Cs=(A[0]+4*u,A[1]); Bs=(Cs[0],A[1]+3*u)
poly(ax,[A,Cb,Bb],'autre',lw=1.2); poly(ax,[A,Cs,Bs],'sujet',lw=1.4)
for C,B,s in ((Cb,Bb,3.2),(Cs,Bs,2.2)):
    line(ax,[(C[0]-s,A[1]),(C[0]-s,A[1]+s),(C[0],A[1]+s)],'encre',lw=0.6)
r=8; ax.add_patch(Arc(A,2*r,2*r,theta1=0,theta2=36.87,color=COL['encre'],lw=0.9,zorder=3))
text(ax,A[0]+2*u,A[1]-3.5,'3, 4, 5','sujet','s')
text(ax,A[0]+6*u,A[1]-3.5,'9, 12, 15','autre','s')
text(ax,A[0]+3,A[1]-9,'36,87°','encre','s')
text(ax,Bb[0]-8,Bb[1]-8,'53,13°','encre','s')
text(ax,Cb[0]-6.5,A[1]+9,'90°','encre','s')
arrow(ax,(Cs[0]+1.5,A[1]+3),(Cb[0]-1.5-4,A[1]+3),'varie')
text(ax,A[0]+7*u/2+10,A[1]+6.5,'× 3','varie','l')
save(fig,'26-008')
