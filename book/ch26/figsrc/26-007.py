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

fig,ax=canvas(50)
cols=[(16,'sin A','3','5','varie','resultat'),(44,'cos A','4','5','sujet','resultat'),(72,'tan A','3','4','varie','sujet')]
for x,n,u,d,ru,rd in cols:
    text(ax,x,46,n,'encre','l')
    text(ax,x,37,u,ru,'l')
    line(ax,[(x-5,32),(x+5,32)],'encre',lw=0.9)
    box(ax,x-6,20.5,12,9,rd,label=d,size='l')
brace(ax,10,50,19,'resultat',label="l'hypoténuse c en bas")
brace(ax,66,78,19,'sujet',label='côté b en bas')
save(fig,'26-007')
