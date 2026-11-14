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

R=44; xo,yo=12,11
fig,ax=canvas(66)
P=quad(ax,xo,yo,R,35,ext=1.0); Bp=(xo,yo+R); S=(xo+R/math.tan(math.radians(35)),yo+R)
line(ax,[Bp,(S[0]+3,Bp[1])],'fixe',lw=0.8,dash=True)
line(ax,[(xo,yo),S],'fixe',lw=1.0)
line(ax,[Bp,S],'sujet',lw=2.4)
for p in [(xo,yo),Bp,S,P]: dot(ax,p)
text(ax,xo-3,yo-3,'O','encre','m'); text(ax,Bp[0]-3,Bp[1]+2,'B','encre','m'); text(ax,S[0],S[1]+3,'S','encre','m'); text(ax,P[0]+3,P[1]-2.5,'P','encre','m')
text(ax,(xo+S[0])/2,Bp[1]+8,r'$\mathrm{cotan}\,\theta$ = BS = 1,4281','sujet','m')
tharc(ax,xo,yo,35); tlab(ax,xo,yo,35)
save(fig,'31-062')
