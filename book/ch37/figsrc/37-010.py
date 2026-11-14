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
line(ax, [C, A], 'sujet', 1.6); line(ax, [B, H], 'resultat', 1.8)
sq(ax, H, (-1, 0), (0, 1), role='resultat')
arrow(ax, (H[0]+5, H[1]+1), (H[0]+5, B[1]-1), 'resultat', both=True)
text(ax, C[0]-2, C[1]-2.5, 'C', 'encre', 'm', ha='right'); text(ax, A[0]+2, A[1]-2.5, 'A', 'encre', 'm', ha='left')
text(ax, B[0], B[1]+3, 'B', 'encre', 'm'); text(ax, H[0], H[1]-3.5, 'H', 'encre', 'm')
text(ax, 44, 12-8, 'base CA (120 m)', 'sujet', 's')
text(ax, H[0]+7, 34, r'$h$ ≈ 87,85 m', 'resultat', 's', ha='left')
text(ax, 44, 62, 'segment BH → nombre h', 'encre', 'm')
save(fig, '37-010')
