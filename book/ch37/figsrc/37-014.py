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
fig, ax = canvas(84)
box(ax, 8, 66, 72, 12, 'sujet', label=r'aire $= \frac{1}{2} \times b \times h$', size='l')
arrow(ax, (44, 65), (44, 56), 'varie', 1.4); text(ax, 48, 60.5, r'$h$ devient $a\,\sin C$', 'varie', 's', ha='left')
box(ax, 8, 42, 72, 12, 'fixe', label=r'aire $= \frac{1}{2} \times b \times a\,\sin C$', size='m')
arrow(ax, (44, 41), (44, 32), 'encre', 1.0)
box(ax, 8, 18, 72, 12, 'resultat', label=r'aire $= \frac{1}{2}\,a\,b\,\sin C$', size='l')
text(ax, 44, 11.5, r'$\frac{1}{2} \times 120 \times 87{,}85 \approx 5\,271$', 'sujet', 's')
text(ax, 44, 5, r'$\frac{1}{2} \times 110 \times 120 \times 0{,}7986 \approx 5\,271$', 'resultat', 's')
save(fig, '37-014')
