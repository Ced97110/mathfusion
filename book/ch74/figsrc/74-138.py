import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 10
def lat(ox, oy, a, b, role, lab):
    lo, hi = ox - 20, ox + 24
    for i in range(-3, 5):
        for j in range(0, 4):
            x, y = ox + i*a[0]*u + j*b[0]*u, oy + i*a[1]*u + j*b[1]*u
            if lo < x < hi and y < 50: disc(ax, x, y, 0.8, 'fixe')
    arrow(ax, (ox, oy), (ox+a[0]*u, oy+a[1]*u), 'sujet', lw=1.3)
    arrow(ax, (ox, oy), (ox+b[0]*u, oy+b[1]*u), 'autre', lw=1.3)
    ang = math.degrees(math.atan2(b[1], b[0]))
    r = 5
    arrow(ax, (ox+r, oy), (ox+r*math.cos(math.radians(ang)), oy+r*math.sin(math.radians(ang))), 'varie', curve=0.4, lw=0.8)
    text(ax, ox+8.5*math.cos(math.radians(ang/2))+1, oy+8.5*math.sin(math.radians(ang/2)), lab, 'varie', 's')
    text(ax, ox+a[0]*u+3, oy-3, r'$x$', 'sujet', 'm')
    text(ax, ox+b[0]*u+3, oy+b[1]*u+2, r'$y$', 'autre', 'm')
    disc(ax, ox, oy, 1.1, 'encre')
lat(20, 14, (1, 0), (0, 1), 'sujet', '90°')
lat(65, 14, (1, 0), (0.5, math.sqrt(3)/2), 'sujet', '60°')
text(ax, 22, 52, 'carré : quart de tour', 'sujet', 's')
text(ax, 66, 52, 'hexagonal : sixième', 'sujet', 's')
line(ax, [(44, 4), (44, 48)], 'fixe', dash=True)
save(fig, '74-138')
