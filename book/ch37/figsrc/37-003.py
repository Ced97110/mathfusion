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
fig, ax = canvas(66)
C, A, B, H = field(0.5, (14, 12))
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'sujet', 1.6); line(ax, [C, B], 'sujet', 1.6); line(ax, [A, B], 'fixe', 1.0, dash=True)
arc(ax, C, 9, 0, 53, 'varie', 1.2)
text(ax, 31, 15.5, '53°', 'varie', 's')
text(ax, 25, 36, '110 m', 'sujet', 's', ha='right')
text(ax, 44, 12-5.5, '120 m', 'sujet', 's')
text(ax, 71, 36, '≈ 103,0 m', 'fixe', 's')
text(ax, 44, 61, 'côté, angle, côté', 'sujet', 'm')
text(ax, 42, 24, 'aire ?', 'fixe', 'm')
save(fig, '37-003')
