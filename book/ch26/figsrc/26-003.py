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

fig,ax=canvas(84)
X,Wb=24,44
box(ax,X,70,Wb,9,'sujet',label='30 m et 26 m')
box(ax,X,54,Wb,9,'varie',label=r'$30^2-26^2=224$')
box(ax,X,38,Wb,9,'varie',label=r'$\sqrt{224}\approx 14{,}97$')
box(ax,X,22,Wb,9,'fixe',label=r'$\tan A=26/14{,}97$')
box(ax,X,3,Wb,10,'resultat',label=r'angle $A$',weight='bold')
for y0,y1 in ((70,63),(54,47),(38,31),(22,13)): arrow(ax,(X+Wb/2,y0),(X+Wb/2,y1),'encre')
text(ax,X+Wb+2,58.5,'détour','varie','m',ha='left')
text(ax,X+Wb+2,45.5,'arrondi','varie','m',ha='left',weight='bold')
text(ax,X+Wb+2,41,'14,9666…\n→ 14,97','varie','s',ha='left')
text(ax,X+Wb+2,26.5,'tangente','fixe','m',ha='left')
line(ax,[(X,74.5),(9,74.5),(9,8)],'resultat',lw=1.4)
arrow(ax,(9,8),(X,8),'resultat',lw=1.4)
text(ax,5,41,'direct','resultat','m',rot=90)
save(fig,'26-003')
