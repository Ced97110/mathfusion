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

fig,ax=canvas(64)
A,B,C=rtri(ax,8,38,36,15,ca='varie',cb='fixe',cc='resultat')
text(ax,46,45.5,'a = 5','varie','m',ha='left')
p=hyp_off(A,B,4.5); text(ax,p[0],p[1]+1,'c = 13','resultat','m')
text(ax,5,36,'A','encre','m')
y=18
text(ax,14,y,'sin A','encre','l'); text(ax,24,y,'=','encre','l')
line(ax,[(28,y),(36,y)],'encre',lw=0.9); text(ax,32,y+4,'a','varie','l'); text(ax,32,y-4,'c','resultat','l')
text(ax,41,y,'=','encre','l')
line(ax,[(44.5,y),(54.5,y)],'encre',lw=0.9); text(ax,49.5,y+4,'5','varie','l'); text(ax,49.5,y-4,'13','resultat','l')
text(ax,73,y,'≈ 0,3846','resultat','l')
save(fig,'26-011')
