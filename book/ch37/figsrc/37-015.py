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
fig, ax = canvas(58)
text(ax, 21, 47, r'$\Delta$', 'fixe', 36)
text(ax, 21, 29, 'chapitre 36', 'fixe', 's'); text(ax, 21, 24.5, 'discriminant', 'fixe', 's')
line(ax, [(44, 12), (44, 54)], 'fixe', 0.6, dash=True)
text(ax, 66, 47, r'$\Delta$', 'sujet', 36)
k = 0.25; C = (50, 17); A = (C[0]+120*k, 17); th = math.radians(53); B = (C[0]+110*math.cos(th)*k, 17+110*math.sin(th)*k)
poly(ax, [C, A, B], 'sujet')
text(ax, 66, 10, 'chapitre 37 : aire', 'sujet', 's')
text(ax, 66, 5, '≈ 5 271 m²', 'resultat', 's')
save(fig, '37-015')
