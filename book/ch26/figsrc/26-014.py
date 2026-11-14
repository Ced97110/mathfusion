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

fig,ax=canvas(72)
A,B,C=rtri(ax,6,44,30,12.5,ca='varie',cb='sujet',cc='resultat',r=7)
text(ax,21,40.5,'12','sujet','m'); text(ax,C[0]+3,50,'5','varie','m',ha='left')
p=hyp_off(A,B,3.2); text(ax,p[0],p[1]+0.5,'13','resultat','m')
text(ax,A[0]+11,A[1]+2.3,'A','encre','m')
cols=[(16,'cosinus','12','13','sujet','resultat','resultat',None),
      (44,'sinus','5','13','varie','resultat','fixe','num'),
      (72,'tangente','5','12','varie','sujet','fixe','den')]
for cx,name,n,d,rn,rd,rb,ch in cols:
    box(ax,cx-12,5,24,29,rb,fill=True)
    text(ax,cx,29,name,'encre','m',weight='bold')
    text(ax,cx,22,n,rn,'l',weight='bold'); line(ax,[(cx-4,17.5),(cx+4,17.5)],'encre',lw=0.9)
    text(ax,cx,12,d,rd,'l',weight='bold')
    if ch=='num': box(ax,cx-3.4,19.2,6.8,5.6,'varie',fill=False,lw=1.3,r=0.6)
    if ch=='den': box(ax,cx-3.4,9.2,6.8,5.6,'varie',fill=False,lw=1.3,r=0.6)
text(ax,62,52,'cerclé : ce qui change\npar rapport au cosinus','varie','s')
save(fig,'26-014')
