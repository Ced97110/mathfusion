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
box(ax, 10, 52, 68, 11, 'sujet', label=r'$\Delta = \frac{1}{2}\,a\,b\,\sin C$', size='l')
def tri(o, k, ang, a, b):
    C = o; A = (o[0]+b*k, o[1]); t = math.radians(ang); B = (o[0]+a*k*math.cos(t), o[1]+a*k*math.sin(t))
    poly(ax, [C, A, B], 'fixe'); line(ax, [C, A], 'sujet', 1.5); line(ax, [C, B], 'sujet', 1.5); arc(ax, C, 4, 0, ang, 'varie', 1.0)
    return C, A, B
C1, A1, B1 = tri((5, 22), 2.6, 90, 6, 8)
tri((34, 22), 2.6, 30, 6, 8)
tri((63, 22), 0.2, 53, 110, 120)
text(ax, 4, 31, 'a', 'sujet', 's', ha='right'); text(ax, 16, 19, 'b', 'sujet', 's'); text(ax, 9, 25, 'C', 'varie', 's')
for x, l1, l2 in [(15, '6 · 8 · 90°', 'Δ = 24'), (44, '6 · 8 · 30°', 'Δ = 12'), (73, '110 · 120 · 53°', 'Δ ≈ 5 271')]:
    text(ax, x, 11, l1, 'varie', 's'); text(ax, x, 5.5, l2, 'resultat', 's')
save(fig, '37-016')
