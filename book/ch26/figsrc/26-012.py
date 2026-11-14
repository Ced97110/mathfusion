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

fig,ax=canvas(66)
Y=38
tris=[(12,10.4,7.8,3.5),(32,20.8,15.6,5.5),(60,20.4,8.5,5.5)]
for x,w,h,r in tris:
    rtri(ax,x,Y,w,h,ca='fixe',cb='sujet',cc='resultat',r=r)
def pol(p,r,a): return (p[0]+r*math.cos(math.radians(a)),p[1]+r*math.sin(math.radians(a)))
for x,w,h,r in tris[:2]:
    a=math.degrees(math.atan2(h,w)); p=pol((x,Y),r+3,a/2); text(ax,p[0],p[1]-0.3,'A','encre','s')
text(ax,17.2,Y-3,'b','sujet','s'); p=hyp_off((12,Y),(22.4,Y+7.8),3); text(ax,p[0],p[1],'c','resultat','s')
text(ax,17.2,Y-12,'4/5 = 0,8','resultat','m'); text(ax,42.4,Y-12,'8/10 = 0,8','resultat','m')
text(ax,70.2,Y-12,'12/13 ≈ 0,9231','autre','m')
brace(ax,12,52.8,Y+22,'resultat',label='même angle',down=False)
text(ax,70,Y+15,'autre angle','autre','s')
text(ax,16,12,r'cos $A$ =','encre','m',ha='left')
text(ax,38,16,'b','sujet','m'); line(ax,[(35,12),(41,12)],'encre',lw=0.8); text(ax,38,8,'c','resultat','m')
text(ax,45,16,'côté adjacent','sujet','m',ha='left'); text(ax,45,8,'hypoténuse','resultat','m',ha='left')
save(fig,'26-012')
