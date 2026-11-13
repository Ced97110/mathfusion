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
fig, ax = canvas(60)
C, A, B, H = field()
poly(ax, [C, A, B], 'sujet')
line(ax, [B, H], 'varie', 1.2, dash=True)
text(ax, 44, 55, 'champ triangulaire', 'sujet', 'm')
text(ax, (C[0]+A[0])/2, C[1]-5.5, 'base : clôture de 120 m', 'sujet', 's')
text(ax, H[0]-2, 36, 'hauteur ?', 'varie', 's', ha='right')
box(ax, 58, 38, 27, 9, 'varie', label='dans le blé', size='s')
save(fig, '37-001')
