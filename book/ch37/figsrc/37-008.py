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
poly(ax, [C, A, B], 'fixe', fill=False)
poly(ax, [C, H, B], 'sujet')
line(ax, [C, B], 'sujet', 1.6); line(ax, [B, H], 'resultat', 1.8)
sq(ax, H, (-1, 0), (0, 1), role='resultat')
arc(ax, C, 8, 0, 53, 'varie', 1.1)
text(ax, 25, 15.5, '53°', 'varie', 's')
text(ax, C[0]-2, C[1]-2.5, 'C', 'encre', 'm', ha='right'); text(ax, A[0]+2, A[1]-2.5, 'A', 'encre', 'm', ha='left')
text(ax, B[0], B[1]+3, 'B', 'encre', 'm'); text(ax, H[0], H[1]-3.5, 'H', 'encre', 'm')
text(ax, 24, 38, 'a = 110', 'sujet', 's', ha='right')
text(ax, H[0]+2, 33, 'h ≈ 87,85', 'resultat', 's', ha='left')
text(ax, 44, 62, r'$h = a\,\sin C$', 'encre', 'l')
save(fig, '37-008')
