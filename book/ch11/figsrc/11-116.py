import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def marks(ax, p, q, n, role='fixe'):
    dx, dy = q[0]-p[0], q[1]-p[1]; L = math.hypot(dx, dy); d = (dx/L, dy/L); nn = (-d[1], d[0])
    mx, my = (p[0]+q[0])/2, (p[1]+q[1])/2
    for k in range(n):
        o = (k-(n-1)/2)*2.0
        c = (mx+d[0]*o, my+d[1]*o); tip = (c[0]+d[0]*0.9, c[1]+d[1]*0.9)
        for s in (1, -1):
            line(ax, [(c[0]-d[0]*0.9+s*nn[0]*1.3, c[1]-d[1]*0.9+s*nn[1]*1.3), tip], role, lw=0.8)
fig, ax = canvas(54)
y0, y1 = 14, 34
T = [(4, y0), (34, y0), (24, y1), (14, y1)]
poly(ax, T, 'sujet'); marks(ax, T[0], T[1], 1, 'sujet'); marks(ax, T[3], T[2], 1, 'sujet')
line(ax, [(14, y0), (14, y1)], 'varie', dash=True)
text(ax, 20, 24, 'h = 4', 'varie', 's')
text(ax, 19, 9, 'b₁ = 6', 'sujet', 's')
text(ax, 19, 39, 'b₂ = 2', 'sujet', 's')
text(ax, 19, 47, 'trapèze', 'sujet')
Q = [(50, y0), (80, y0), (84, y1), (54, y1)]
poly(ax, Q, 'autre'); marks(ax, Q[0], Q[1], 1, 'autre'); marks(ax, Q[3], Q[2], 1, 'autre')
marks(ax, Q[1], Q[2], 2, 'autre'); marks(ax, Q[0], Q[3], 2, 'autre')
text(ax, 65, 9, '6', 'autre', 's')
text(ax, 69, 39, '6', 'autre', 's')
text(ax, 67, 47, 'trapèze aussi', 'autre')
save(fig, '11-116')
