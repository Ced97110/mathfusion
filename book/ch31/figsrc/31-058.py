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

R=50; xo,yo=14,12
fig,ax=canvas(66)
P=quad(ax,xo,yo,R,35); H=(P[0],yo)
poly(ax,[(xo,yo),H,P],'fixe')
line(ax,[(xo,yo),H],'sujet',lw=2.4)
line(ax,[H,P],'fixe',lw=1.0); line(ax,[(xo,yo),P],'fixe',lw=1.0)
line(ax,[(H[0]-3,yo),(H[0]-3,yo+3),(H[0],yo+3)],'fixe',lw=0.6)
for p in [(xo,yo),H,P,(xo+R,yo)]: dot(ax,p)
text(ax,xo-3,yo-3,'O','encre','m'); text(ax,H[0],yo-3,'H','encre','m'); text(ax,xo+R+2.5,yo-3,'A','encre','m'); text(ax,P[0]+3,P[1]+2.5,'P','encre','m')
text(ax,(xo+H[0])/2,yo-8,r'$\cos\theta$ = OH = 0,8192','sujet','m')
text(ax,(xo+P[0])/2-3,(yo+P[1])/2+3.5,'1','fixe','m')
tharc(ax,xo,yo,35); tlab(ax,xo,yo,35)
save(fig,'31-058')
