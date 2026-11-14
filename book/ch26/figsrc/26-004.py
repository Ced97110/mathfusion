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

fig,ax=canvas(62)
A,B,C=rtri(ax,8,10,24,41.6,ca='varie',cb='sujet',cc='resultat',db=True)
text(ax,C[0]+2,10+20.8,'26 m','varie','m',ha='left')
text(ax,20,5.5,'?','sujet','l')
p=hyp_off(A,B,4.5); text(ax,p[0],p[1],'30 m','resultat','m')
arrow(ax,(46,36),(54,36),'encre')
box(ax,56,28,28,16,'resultat',label=r'$\frac{26}{30}$',size='l')
text(ax,70,22,r'$=0{,}8666\ldots$','resultat','m')
text(ax,70,15,'aucune autre mesure','fixe','s')
save(fig,'26-004')
