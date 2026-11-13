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
fig, ax = canvas(68)
ox, oy = 14, 29
Ap = (ox, oy); Bp = (ox+60, oy); Cx = 37.5; Cp = (ox+Cx, oy+math.sqrt(2500-Cx**2))
O = (ox+30, oy+3.77); I = (ox+35, oy+13.23)
disc(ax, O[0], O[1], 30.24, 'sujet', fill=False, lw=1.0)
disc(ax, I[0], I[1], 13.23, 'autre', fill=True, lw=1.0)
poly(ax, [Ap, Bp, Cp], 'fixe', fill=False, lw=1.0)
disc(ax, O[0], O[1], 1.0, 'sujet'); 
text(ax, O[0]-1, O[1]-5.5, 'puits', 'sujet', 's', ha='right')
text(ax, I[0]+1, I[1]+0.5, 'mare', 'autre', 's')
for p in (Ap, Bp, Cp): line(ax, [O, p], 'sujet', 0.7, dash=True)
text(ax, 44, 64, 'deux cercles, un champ', 'encre', 'm')
save(fig, '37-005')
