import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
cx, cy, R = 44, 48, 22
names = ['1', r'$r$', r'$r^2$', r'$r^3$', r'$s$', r'$rs$', r'$r^2s$', r'$r^3s$']
pos = [(cx + R*math.cos(math.radians(90 - i*45)), cy + R*math.sin(math.radians(90 - i*45))) for i in range(8)]
c = pos[2]
for i, p in enumerate(pos):
    if i == 2: continue
    d = math.hypot(p[0]-c[0], p[1]-c[1]); ux, uy = (p[0]-c[0])/d, (p[1]-c[1])/d
    arrow(ax, (c[0]+ux*5, c[1]+uy*5), (p[0]-ux*5, p[1]-uy*5), 'resultat', both=True, lw=0.8)
for i, (p, l) in enumerate(zip(pos, names)):
    disc(ax, p[0], p[1], 4.4, 'sujet' if i == 2 else 'fixe', label=l, size='s')
text(ax, cx, 10, r'$sr^2s=r^2$', 'sujet', 'l')
text(ax, cx, 3.5, 'commute avec les 8 : dans le centre', 'resultat', 'm')
save(fig, '49-276')
