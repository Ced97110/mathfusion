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
A1,B1,C1=rtri(ax,8,26,12.8,9.6)
text(ax,C1[0]+2,26+4.8,'3','varie','m',ha='left'); text(ax,14.4,22.8,'4','sujet','m')
p=hyp_off(A1,B1,3.5); text(ax,p[0],p[1],'5','resultat','m')
A2,B2,C2=rtri(ax,40,26,25.6,19.2)
text(ax,C2[0]+2,26+9.6,'6','varie','m',ha='left'); text(ax,52.8,22.8,'8','sujet','m')
p=hyp_off(A2,B2,3.5); text(ax,p[0],p[1],'10','resultat','m')
box(ax,2,7,30,11,'resultat',label=r'$3/5=0{,}6$')
box(ax,38,7,30,11,'resultat',label=r'$6/10=0{,}6$')
text(ax,35,12.5,'=','resultat','l')
text(ax,36,51,'mêmes angles','encre','m')
save(fig,'26-009')
