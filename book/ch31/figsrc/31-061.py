import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def quad(ax, xo, yo, R, deg, ext=1.05):
    pts = [(xo + R*math.cos(math.radians(a)), yo + R*math.sin(math.radians(a))) for a in range(0, 91, 3)]
    line(ax, pts, 'fixe', lw=0.8)
    line(ax, [(xo - 2, yo), (xo + R*ext, yo)], 'fixe', lw=0.6)
    line(ax, [(xo, yo - 2), (xo, yo + R*ext)], 'fixe', lw=0.6)
    t = math.radians(deg)
    return (xo + R*math.cos(t), yo + R*math.sin(t))

def dot(ax, p, role='encre', r=0.8):
    ax.add_patch(Circle(p, r, fc=COL[role], ec=COL[role], zorder=6))

def tharc(ax, xo, yo, deg, r=9, role='varie'):
    line(ax, [(xo + r*math.cos(math.radians(deg*i/20)), yo + r*math.sin(math.radians(deg*i/20))) for i in range(21)], role, lw=1.0)

def tlab(ax, xo, yo, deg, r=13, s=r'$\theta$'):
    a = math.radians(deg/2); text(ax, xo + r*math.cos(a), yo + r*math.sin(a), s, 'varie', 'm')

R=30; xo,yo=12,10
fig,ax=canvas(70)
P=quad(ax,xo,yo,R,60,ext=1.0); A=(xo+R,yo); T=(A[0],yo+R*math.tan(math.radians(60)))
line(ax,[A,T],'fixe',lw=0.8,dash=True)
line(ax,[(xo,yo),T],'sujet',lw=2.4)
H=(P[0],yo); line(ax,[P,H],'fixe',lw=0.8)
for p in [(xo,yo),A,T,P]: dot(ax,p)
text(ax,xo-3,yo-3,'O','encre','m'); text(ax,A[0]+2.5,yo-3,'A','encre','m'); text(ax,T[0]+2.5,T[1]+1,'T','encre','m'); text(ax,P[0]-3.2,P[1]+2.5,'P','encre','m')
text(ax,H[0],yo-3,r'$\cos\theta$ = 0,5','fixe','s')
text(ax,A[0]+6,yo+30,r'$\sec\theta$ = OT','sujet','m',ha='left')
text(ax,A[0]+6,yo+24,r'$= 1/0{,}5 = 2$','sujet','m',ha='left')
tharc(ax,xo,yo,60,r=8); tlab(ax,xo,yo,60,r=11)
save(fig,'31-061')
