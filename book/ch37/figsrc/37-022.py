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
cols = [16, 44, 72]
for x, t in zip(cols, ['hauteur', 'rectangle', 'moitié']):
    text(ax, x, 59, t, 'encre', 'm', weight='bold')
# 1 bar of height
hh = 87.85*0.25
box(ax, 13, 22, 6, hh, 'sujet')
# 2 rectangle
poly(ax, [(34, 22), (34+120*0.2, 22), (34+120*0.2, 22+hh), (34, 22+hh)], 'fixe')
# 3 rectangle with triangle
o = 62; poly(ax, [(o, 22), (o+24, 22), (o+24, 22+hh), (o, 22+hh)], 'fixe')
poly(ax, [(o, 22), (o+24, 22), (o+13.24*0+ (66.2/120)*24, 22+hh)], 'resultat')
for x, a, b in [(16, r'$a\,\sin C$', '≈ 87,85'), (44, r'$b \times h$', '≈ 10 542'), (72, r'$\frac{1}{2}$', '≈ 5 271')]:
    text(ax, x, 14, a, 'varie', 's'); text(ax, x, 8.5, b, 'resultat', 's')
arrow(ax, (24, 35), (31, 35), 'encre', 0.9)
save(fig, '37-022')
