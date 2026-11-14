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

fig,ax=canvas(54)
A,B,C=rtri(ax,4,10,26,19.5,ca='varie',cb='fixe',cc='resultat',r=6)
text(ax,C[0]+2,19.5,'opposé 3','varie','s',ha='left'); text(ax,17,6.5,'adjacent 4','fixe','s')
p=hyp_off(A,B,5); text(ax,p[0]-3,p[1],'hypoténuse 5','resultat','s')
text(ax,A[0]+10,A[1]+3.2,'A','encre','m')
for y,l,n,r in ((38,r'$3/5=0{,}6$','sinus','resultat'),(23,r'$4/5=0{,}8$','cosinus','fixe'),(8,r'$3/4=0{,}75$','tangente','fixe')):
    box(ax,46,y,24,9,r,label=l)
    text(ax,73,y+6.5 if r=='resultat' else y+4.5,n,r,'m',ha='left',weight='bold' if r=='resultat' else 'normal')
text(ax,73,38+3.2,'opposé','varie','s',ha='left'); text(ax,73,38+0.2,'hypoténuse','resultat','s',ha='left')
save(fig,'26-013')
