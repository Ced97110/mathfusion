import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role='varie', lw=0.9):
    line(ax, [(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/30)), c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/30))) for i in range(31)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    line(ax, [(p[0]+d1[0]*s, p[1]+d1[1]*s), (p[0]+(d1[0]+d2[0])*s, p[1]+(d1[1]+d2[1])*s), (p[0]+d2[0]*s, p[1]+d2[1]*s)], role, 0.7)
fig, ax = canvas(84)
k = 0.26; th = math.radians(53)
C = (8, 30); H = (C[0]+110*math.cos(th)*k, 30); B = (H[0], 30+110*math.sin(th)*k)
poly(ax, [C, H, B], 'sujet'); line(ax, [B, H], 'resultat', 1.8); line(ax, [C, B], 'sujet', 1.5)
sq(ax, H, (-1, 0), (0, 1), s=2.0, role='fixe'); arc(ax, C, 7, 0, 53, 'varie', 1.2)
text(ax, C[0]+10.5, C[1]+2.5, 'C', 'varie', 's', weight='bold')
text(ax, H[0], H[1]-3, 'H', 'encre', 's'); text(ax, B[0], B[1]+3, 'B', 'encre', 's')
text(ax, H[0]+2, 42, 'h', 'resultat', 's', ha='left'); text(ax, 9, 44, 'a', 'sujet', 's', ha='right')
X, Wd = 36, 50
box(ax, X, 66, Wd, 13, 'sujet', label=r'$\sin C = \frac{h}{a}$', size='l')
arrow(ax, (X+Wd/2, 65), (X+Wd/2, 55), 'varie', 1.4)
text(ax, X+Wd/2+2, 60, '× a', 'varie', 'm', ha='left', weight='bold')
box(ax, X, 40, Wd, 13, 'varie', label=r'$a \times \sin C = a \times \frac{h}{a}$', size='m')
arrow(ax, (X+Wd/2, 39), (X+Wd/2, 29), 'varie', 1.4)
text(ax, X+Wd/2+2, 34, 'a se simplifie', 'varie', 's', ha='left')
box(ax, X, 14, Wd, 13, 'resultat', label=r'$h = a\,\sin C$', size='l')
text(ax, 20, 14, '87,85 ÷ 110 = 0,7986', 'fixe', 's'); text(ax, 20, 8, '110 × 0,7986 = 87,85', 'fixe', 's')
save(fig, '37-011')
