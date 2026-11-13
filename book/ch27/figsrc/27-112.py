import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(60)
k = 36; A = (5, 14); B = (5, 44)
for P0, ang, role in ((B, 20, 'sujet'), (A, 12.7, 'varie')):
    a = math.radians(ang); e = (P0[0] + k * math.cos(a), P0[1] + k * math.sin(a))
    line(ax, [P0, (e[0], P0[1])], 'fixe', lw=0.6, dash=True); line(ax, [P0, e], role, lw=1.8)
    line(ax, [(e[0], P0[1]), e], 'resultat', lw=1.8)
    disc(ax, e[0], e[1], 1.0, role); disc(ax, e[0], P0[1], 0.8, 'fixe')
text(ax, 22, 37, '1 m sur la plus grande pente', 'sujet', 's'); text(ax, 22, 7.5, '1 m en biais à 50°', 'varie', 's')
text(ax, 46, 50, r'$0{,}3420$ m $=\sin\theta$', 'resultat', 's', ha='left')
text(ax, 46, 20, r'$0{,}2198$ m', 'resultat', 's', ha='left')
text(ax, 54, 31, 'hauteur gagnée', 'resultat', 's', ha='left') if False else None
arrow(ax, (73, 44), (73, 25), 'varie'); text(ax, 75, 36, r'$\times\cos\varphi$', 'varie', 's', ha='left'); text(ax, 75, 32.5, '0,6428', 'varie', 's', ha='left')
save(fig, '27-112')
