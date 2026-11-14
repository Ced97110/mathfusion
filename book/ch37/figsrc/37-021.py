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
k = 0.5; O = (24, 10)
C, A, B, H = field(k, O)
h = 87.85*k
poly(ax, [(O[0], O[1]), (O[0]+60, O[1]), (O[0]+60, O[1]+h), (O[0], O[1]+h)], 'fixe')
poly(ax, [C, A, B], 'sujet')
text(ax, B[0], O[1]+h+3, 'rectangle b × h ≈ 10 542', 'fixe', 's')
text(ax, B[0], O[1]+13, 'triangle', 'sujet', 'm')
text(ax, B[0], O[1]+8.5, '½ ≈ 5 271', 'sujet', 's')
text(ax, 54, 4, 'b = 120 m', 'encre', 's')
text(ax, 22, O[1]+h/2, 'h ≈ 87,85', 'encre', 's', ha='right')
save(fig, '37-021')
