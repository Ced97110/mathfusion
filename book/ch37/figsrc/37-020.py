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
fig, ax = canvas(78)
k = 0.3; th = math.radians(53)
C = (12, 40); H = (C[0]+110*math.cos(th)*k, 40); B = (H[0], 40+110*math.sin(th)*k)
poly(ax, [C, H, B], 'sujet'); line(ax, [B, H], 'resultat', 1.8); line(ax, [C, B], 'sujet', 1.5)
sq(ax, H, (-1, 0), (0, 1), s=2.0, role='fixe'); arc(ax, C, 6, 0, 53, 'varie', 1.0)
text(ax, H[0]+3, 53, 'h ≈ 87,85', 'resultat', 's', ha='left'); text(ax, 18, 57, 'a = 110', 'sujet', 's', ha='right')
text(ax, 62, 66, r'$\sin C = \frac{h}{a}$', 'encre', 'l')
text(ax, 62, 40, 'm ÷ m : sans unité', 'fixe', 's')
f = numberline(ax, 10, 70, 18, 0, 1, 0.1, every=5, arrow_right=False)
disc(ax, f(0.7986), 18, 1.5, 'resultat')
arrow(ax, (f(0.7986), 29), (f(0.7986), 20.5), 'resultat', 1.0)
text(ax, f(0.7986), 32, '87,85 ÷ 110 ≈ 0,7986', 'resultat', 's')
save(fig, '37-020')
