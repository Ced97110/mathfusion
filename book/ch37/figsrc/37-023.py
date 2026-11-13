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
fig, ax = canvas(82)
C, A, B, H = field(0.5, (14, 28))
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'sujet', 1.6); line(ax, [C, B], 'sujet', 1.6)
arc(ax, C, 9, 0, 53, 'resultat', 1.6)
arc(ax, A, 7, 180-58.52, 180, 'fixe', 1.2)
text(ax, 30, 31.5, '53°', 'resultat', 's')
text(ax, A[0]-14, A[1]+5, '58,52°', 'fixe', 's')
text(ax, B[0]+10, B[1]-2, '68,48°', 'fixe', 's')
text(ax, 24, 54, '110', 'sujet', 's', ha='right'); text(ax, 44, 28-5.5, '120', 'sujet', 's')
box(ax, 4, 4, 38, 12, 'resultat', label='53° → 5 271', size='s')
box(ax, 46, 4, 38, 12, 'limite', label='58,52° → 5 628', size='s')
text(ax, 44, 79, 'angle entre les deux côtés', 'sujet', 's')
save(fig, '37-023')
