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

fig,ax=canvas(58)
A,B,C=rtri(ax,14,12,44,33,ca='varie',cb='sujet',cc='resultat')
line(ax,[C,B],'varie',lw=2.4)
text(ax,A[0]-3.5,A[1]-3.5,'A','encre','m',weight='bold'); text(ax,C[0]+3,C[1]-3.5,'C','encre','m'); text(ax,B[0]+3,B[1]+3,'B','encre','m')
text(ax,C[0]+2,12+16.5,'a = 3','varie','m',ha='left',weight='bold')
text(ax,36,7.5,'b','sujet','m')
p=hyp_off(A,B,4); text(ax,p[0],p[1],'c','resultat','m')
arrow(ax,(23,15.4),(56.5,27.9),'varie',lw=0.8)
text(ax,38.8,24.2,'en face de A','varie','s',rot=20.5)
save(fig,'26-016')
