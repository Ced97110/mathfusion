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

R=50; xo,yo=14,11
fig,ax=canvas(70)
P=quad(ax,xo,yo,R,35)
sec=[(xo,yo)]+[(xo+R*math.cos(math.radians(35*i/20)),yo+R*math.sin(math.radians(35*i/20))) for i in range(21)]
poly(ax,sec,'sujet')
line(ax,[(xo,yo),(xo+R,yo)],'fixe',lw=1.0); line(ax,[(xo,yo),P],'fixe',lw=1.0)
tharc(ax,xo,yo,35,r=12,role='sujet')
text(ax,xo+20,yo+5.5,r'$\theta$','sujet','l')
for p in [(xo,yo),P,(xo+R,yo)]: dot(ax,p)
text(ax,xo-3,yo-3,'O','encre','m'); text(ax,xo+R+2.5,yo-3,'A','encre','m'); text(ax,P[0]+3,P[1]+2.5,'P','encre','m')
text(ax,xo+R/2,yo-6.5,'OA','fixe','s'); text(ax,xo+R*0.5*math.cos(math.radians(35))-2.8,yo+R*0.5*math.sin(math.radians(35))+4.0,'OP','fixe','s',rot=35)
text(ax,50,66,r'$\theta$ = angle AOP (ici 35°)','sujet','m')
save(fig,'31-056')
