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
u=3.2; A=(6,12)
for k in (3,2,1):
    w,h=4*k*u,3*k*u
    poly(ax,[A,(A[0]+w,A[1]),(A[0]+w,A[1]+h)],'sujet',lw=1.0)
    s=2.4; line(ax,[(A[0]+w-s,A[1]),(A[0]+w-s,A[1]+s),(A[0]+w,A[1]+s)],'encre',lw=0.6)
    text(ax,A[0]+w-4.5,A[1]+h+3.5,f'{5*k} m','resultat','s')
    text(ax,A[0]+w+1.5,A[1]+h/2,f'{3*k} m','varie','s',ha='left')
r=7; ax.add_patch(Arc(A,2*r,2*r,theta1=0,theta2=36.87,color=COL['encre'],lw=0.9,zorder=3))
text(ax,A[0]+9.5,A[1]+2.2,'A','encre','s')
for y,l in zip((50,42,34),(r'$3/5=0{,}6$',r'$6/10=0{,}6$',r'$9/15=0{,}6$')):
    text(ax,70,y,l,'resultat','m')
save(fig,'26-010')
