import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def marks(ax, p, q, n, role='fixe'):
    dx, dy = q[0]-p[0], q[1]-p[1]; L = math.hypot(dx, dy); d = (dx/L, dy/L); nn = (-d[1], d[0])
    mx, my = (p[0]+q[0])/2, (p[1]+q[1])/2
    for k in range(n):
        o = (k-(n-1)/2)*2.0
        c = (mx+d[0]*o, my+d[1]*o); tip = (c[0]+d[0]*0.9, c[1]+d[1]*0.9)
        for s in (1, -1):
            line(ax, [(c[0]-d[0]*0.9+s*nn[0]*1.3, c[1]-d[1]*0.9+s*nn[1]*1.3), tip], role, lw=0.8)
def shape(ax, P, role):
    poly(ax, P, role)
    marks(ax, P[0], P[1], 1, role); marks(ax, P[3], P[2], 1, role)
    marks(ax, P[1], P[2], 2, role); marks(ax, P[0], P[3], 2, role)
fig, ax = canvas(52)
y0, h, w, dx = 14, 25, 26, 10
dy = math.sqrt(h*h-dx*dx)
shape(ax, [(4, y0), (4+w, y0), (4+w, y0+h), (4, y0+h)], 'fixe')
x1 = 48
shape(ax, [(x1, y0), (x1+w, y0), (x1+w+dx, y0+dy), (x1+dx, y0+dy)], 'sujet')
arrow(ax, (34, 26), (44, 26), 'varie')
text(ax, 39, 31, 'on penche', 'varie', 's')
text(ax, 17, 8, 'rectangle', 'fixe')
text(ax, 66, 8, 'parallélogramme', 'sujet')
text(ax, 44, 46, 'marques égales = parallèles', 'fixe', 's')
save(fig, '11-113')
