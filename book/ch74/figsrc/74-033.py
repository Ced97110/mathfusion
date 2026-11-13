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
s=4.0
def tri(o,ang,mir,role,labs):
    pts=tf([(0,0),(4*s,0),(0,3*s)],o,ang,mir); poly(ax,pts,role)
    cx=sum(p[0] for p in pts)/3; cy=sum(p[1] for p in pts)/3
    for (i,j),t in zip([(0,1),(0,2),(1,2)],labs):
        mx=(pts[i][0]+pts[j][0])/2; my=(pts[i][1]+pts[j][1])/2
        dx,dy=mx-cx,my-cy; n=math.hypot(dx,dy)
        text(ax,mx+dx/n*2.6,my+dy/n*2.6,t,role,'s')
tri((8,36),0,False,'sujet',['4','3','5'])
tri((50,36),90,False,'varie',['4','3','5'])
tri((36,6),0,True,'varie',['4','3','5'])
arrow(ax,(28,46),(38,46),'varie'); text(ax,33,50,'tourné','varie','s')
arrow(ax,(14,31),(22,19),'varie'); text(ax,9,24,'retourné','varie','s')
for cy,role in ((48,'sujet'),(16,'varie')):
    disc(ax,72,cy,8,role); line(ax,[(72,cy),(80,cy)],role); text(ax,76,cy+2.2,'2',role,'s')
arrow(ax,(72,38),(72,26),'varie'); text(ax,80,32,'déplacé','varie','s')
save(fig,'74-033')
