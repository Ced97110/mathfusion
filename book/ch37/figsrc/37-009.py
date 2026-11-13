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
line(ax, [C, A], 'sujet', 1.6); line(ax, [B, H], 'fixe', 1.0, dash=True)
sq(ax, H, (-1, 0), (0, 1), role='sujet')
disc(ax, H[0], H[1], 1.6, 'sujet')
text(ax, C[0]-2, C[1]-2.5, 'C', 'encre', 'm', ha='right'); text(ax, A[0]+2, A[1]-2.5, 'A', 'encre', 'm', ha='left')
text(ax, B[0], B[1]+3, 'B', 'encre', 'm'); text(ax, H[0]+1, H[1]-5, 'H', 'sujet', 'l', weight='bold')
brace(ax, C[0], H[0], 6, 'varie', 'CH ≈ 66,2 m')
text(ax, 62, 40, 'pied de la', 'sujet', 's'); text(ax, 62, 36.5, 'perpendiculaire', 'sujet', 's')
save(fig, '37-009')
