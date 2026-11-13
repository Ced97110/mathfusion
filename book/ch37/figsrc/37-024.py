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
k = 0.42; C = (36, 12)
B = (C[0]-66.2*k, C[1]+87.85*k); A = (C[0]+120*k, C[1]); H = (B[0], C[1])
poly(ax, [C, A, B], 'sujet')
line(ax, [H, C], 'fixe', 1.0, dash=True); line(ax, [B, H], 'resultat', 1.8)
sq(ax, H, (1, 0), (0, 1), role='fixe')
arc(ax, C, 8, 0, 127, 'sujet', 1.4); arc(ax, C, 5, 127, 180, 'varie', 1.4)
text(ax, C[0]+11, C[1]+10, '127°', 'sujet', 's', ha='left'); text(ax, C[0]-11, C[1]+3.5, '53°', 'varie', 's')
text(ax, B[0]+1.5, B[1]-25, 'h ≈ 87,85', 'resultat', 's', ha='left')
text(ax, H[0], H[1]-3.5, 'H hors du triangle', 'fixe', 's', ha='left')
text(ax, 44, 58, r'$\sin 127° = \sin 53° \approx 0{,}7986$', 'encre', 's')
save(fig, '37-024')
