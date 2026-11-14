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

fig,ax=canvas(96)
th=math.radians
def mk(yb,deg,kind,s,form):
    t=th(deg); O=(6,yb)
    if kind=='adj':   # adj connu, hyp cherchee
        A=s*4; hyp=A/math.cos(t); opp=A*math.tan(t)
    elif kind=='oppshadow':  # opp connu 3, adj cherche
        opp=s*3; A=opp/math.tan(t); hyp=opp/math.sin(t)
    else:
        opp=s*10; hyp=opp/math.sin(t); A=opp/math.tan(t)
    Bp=(6+A,yb); Cp=(6+A,yb+opp)
    poly(ax,[O,Bp,Cp],'fixe')
    return O,Bp,Cp
# rangee 1 : poutre = 4 x sec 30
O,Bp,Cp=mk(76,30,'adj',6.5,'')
line(ax,[O,Bp],'sujet',lw=2.4); line(ax,[O,Cp],'resultat',lw=2.4)
text(ax,(O[0]+Bp[0])/2,76-3.2,'4','sujet','m')
text(ax,(O[0]+Cp[0])/2-4,(O[1]+Cp[1])/2+4,'poutre','resultat','s')
text(ax,66,76+1,r'$4\times\mathrm{sec}\,30^\circ \approx 4{,}62$','encre','m')
# rangee 2 : ombre = 3 x cotan 40
O,Bp,Cp=mk(44,40,'oppshadow',6.0,'')
line(ax,[O,Bp],'resultat',lw=2.4); line(ax,[Bp,Cp],'sujet',lw=2.4)
text(ax,(O[0]+Bp[0])/2,44-3.2,'ombre','resultat','s')
text(ax,Bp[0]+3,(Bp[1]+Cp[1])/2,'3','sujet','m')
text(ax,66,45,r'$3\times\mathrm{cotan}\,40^\circ \approx 3{,}58$','encre','m')
# rangee 3 : cable = 10 x cosec 25
O,Bp,Cp=mk(12,25,'oppcable',1.4,'')
line(ax,[O,Cp],'resultat',lw=2.4); line(ax,[Bp,Cp],'sujet',lw=2.4)
text(ax,(O[0]+Cp[0])/2-5,(O[1]+Cp[1])/2+4,'câble','resultat','s')
text(ax,Bp[0]+3.5,(Bp[1]+Cp[1])/2,'10','sujet','m')
text(ax,66,13,r'$10\times\mathrm{cosec}\,25^\circ \approx 23{,}66$','encre','m')
save(fig,'31-050')
