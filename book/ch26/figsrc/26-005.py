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

fig,ax=canvas(98)
text(ax,44,93,"mesuré : l'hypoténuse",'resultat','l')
rows=[(66,'échelle','on lit les graduations'),(38,'route','on lit le compteur'),(10,'câble','on déroule le câble')]
for y0,n,m in rows:
    A,B,C=rtri(ax,6,y0,26,16,ca='fixe',cb='fixe',cc='resultat',lw=1.4,da=True,db=True)
    line(ax,[A,B],'resultat',lw=2.4)
    text(ax,C[0]+2.5,y0+8,'?','fixe','m',ha='left')
    text(ax,19,y0-3.5,'?','fixe','m')
    text(ax,44,y0+11,n,'encre','l',ha='left',weight='bold')
    text(ax,44,y0+4,m,'fixe','m',ha='left')
save(fig,'26-005')
