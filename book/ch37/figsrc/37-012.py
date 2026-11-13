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
labs = [('sujet', r'$a = 110$ m ; $C = 53°$'), ('fixe', r'$\sin 53° \approx 0{,}7986$'), ('varie', r'$h = a \times \sin C$'), ('resultat', r'$110 \times 0{,}7986 \approx 87{,}85$ m')]
ys = [62, 45, 28, 11]
for (r, t), y in zip(labs, ys):
    box(ax, 10, y, 68, 12, r, label=t, size='m')
for y in ys[1:]:
    arrow(ax, (44, y+17+0), (44, y+12.8), 'encre', 1.0)
save(fig, '37-012')
