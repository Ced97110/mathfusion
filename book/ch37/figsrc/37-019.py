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
C, A, B, H = field(0.5, (14, 12))
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'sujet', 1.5); line(ax, [C, B], 'sujet', 1.5)
arc(ax, C, 9, 0, 53, 'varie', 1.6)
disc(ax, C[0], C[1], 1.4, 'varie')
text(ax, 24, 38, 'a = 110', 'sujet', 's', ha='right'); text(ax, 44, 12-5.5, 'b = 120', 'sujet', 's')
text(ax, 62, 22, 'angle C = 53°', 'varie', 's')
arrow(ax, (54, 20), (C[0]+9.5, C[1]+4.5), 'varie', 0.8)
text(ax, 9, 6.5, 'coin C', 'encre', 's')
arrow(ax, (12, 8.5), (C[0]-1, C[1]-1), 'encre', 0.8)
text(ax, 44, 58, 'entre a et b', 'encre', 'm')
save(fig, '37-019')
