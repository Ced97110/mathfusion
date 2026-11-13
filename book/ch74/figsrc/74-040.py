import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def Pm(ox, oy, s): return lambda x, y: (ox + x * s, oy + y * s)
def axes(ax, P, x0, x1, y0, y1):
    line(ax, [P(x0, 0), P(x1, 0)], 'fixe', lw=0.5); line(ax, [P(0, y0), P(0, y1)], 'fixe', lw=0.5)
def dot(ax, p, role, r=1.1): disc(ax, p[0], p[1], r, role)
def arc(ax, c, r, a0, a1, role, lw=1.0):
    n = 24; pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-3], pts[-1], role, lw=lw)
def tf(pts, o, ang=0, mir=False):
    a = math.radians(ang); out = []
    for x, y in pts:
        if mir: x = -x
        out.append((o[0] + x * math.cos(a) - y * math.sin(a), o[1] + x * math.sin(a) + y * math.cos(a)))
    return out

fig,ax=canvas(62)
P=Pm(36,16,8); o=P(0,0); r=8*math.sqrt(10)
axes(ax,P,-3.6,4.4,-0.8,4.4)
line(ax,[(o[0]+r*math.cos(math.radians(t)),o[1]+r*math.sin(math.radians(t))) for t in range(0,121,4)],'fixe',lw=0.7,dash=True)
a=P(3,1); b=P(-1,3)
arrow(ax,o,a,'sujet',lw=1.2); arrow(ax,o,b,'resultat',lw=1.2); dot(ax,o,'fixe',1.1)
ang=math.degrees(math.atan2(1,3)); arc(ax,o,9,ang+3,ang+87,'varie')
text(ax,o[0]+9,o[1]+13,'quart de tour','varie','s',ha='left')
text(ax,a[0]+3,a[1]-1,'(3 ; 1)','sujet','s',ha='left'); text(ax,b[0]-3,b[1]+3,'(−1 ; 3)','resultat','s',ha='right')
text(ax,o[0]+2,o[1]-4.5,r'$g(0)=0$','fixe','s')
text(ax,70,8,r'$|x|=|g(x)|=\sqrt{10}$','encre','m')
save(fig,'74-040')
