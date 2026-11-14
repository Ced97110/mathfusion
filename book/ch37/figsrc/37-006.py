import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role='varie', lw=0.9):
    line(ax, [(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/30)), c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/30))) for i in range(31)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    line(ax, [(p[0]+d1[0]*s, p[1]+d1[1]*s), (p[0]+(d1[0]+d2[0])*s, p[1]+(d1[1]+d2[1])*s), (p[0]+d2[0]*s, p[1]+d2[1]*s)], role, 0.7)
def field(k=0.5, O=(14, 10)):
    th = math.radians(53)
    C = O; A = (O[0]+120*k, O[1]); B = (O[0]+110*math.cos(th)*k, O[1]+110*math.sin(th)*k); H = (B[0], O[1])
    return C, A, B, H
fig, ax = canvas(62)
cols = [16, 44, 72]
for x, t1, t2 in [(cols[0], '2 côtés', '+ 1 angle'), (cols[1], '3 côtés', 'seuls'), (cols[2], '2 cercles', 'du triangle')]:
    text(ax, x, 56, t1, 'sujet', 'm', weight='bold'); text(ax, x, 51.5, t2, 'sujet', 's')
# 1: two sides and angle
c = (6, 22); a = (c[0]+22, c[1]); b = (c[0]+22*math.cos(math.radians(53))*0.9, c[1]+22*math.sin(math.radians(53))*0.9)
poly(ax, [c, a, b], 'fixe'); line(ax, [c, a], 'sujet', 1.5); line(ax, [c, b], 'sujet', 1.5); arc(ax, c, 6, 0, 53, 'varie', 1.1)
# 2: three sides
p = [(34, 22), (56, 22), (50, 40)]
poly(ax, p, 'fixe')
for i in range(3): line(ax, [p[i], p[(i+1)%3]], 'sujet', 1.5)
# 3: two circles
q = [(62, 22), (84, 22), (72, 40)]
poly(ax, q, 'fixe', fill=False)
disc(ax, 73, 28, 11.2, 'sujet', fill=False, lw=1.0)
disc(ax, 73, 25, 5, 'autre', fill=True, lw=1.0)
for x, t in [(cols[0], 'aire par'), (cols[1], 'aire par'), (cols[2], 'puits et mare')]:
    pass
text(ax, cols[0], 12, 'besoin 1', 'fixe', 's'); text(ax, cols[1], 12, 'besoin 2', 'fixe', 's'); text(ax, cols[2], 12, 'besoin 3', 'fixe', 's')
save(fig, '37-006')
