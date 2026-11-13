import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(72)
u = 3.5
C = (8, 38); Bp = (C[0] + 6 * u, 38); T = pol(C, 10 * u, 30); Hf = (T[0], 38)
poly(ax, [C, Bp, T], 'resultat')
line(ax, [Bp, Hf], 'fixe', dash=True)
line(ax, [C, Bp], 'autre', lw=2.0); line(ax, [C, T], 'sujet', lw=1.6); line(ax, [Bp, T], 'sujet', lw=1.0)
line(ax, [T, Hf], 'varie', lw=1.6)
sq(ax, Hf, (-1, 0), (0, 1))
arc(ax, C, 9, 0, 30, 'varie'); text(ax, 20, 41, '30°', 'varie', 's')
text(ax, 14, 32.5, 'a = 6', 'autre', 's', ha='left')
text(ax, 17, 52, 'b = 10', 'sujet', 's', rot=30)
text(ax, Hf[0] + 5, 46, 'h = 5', 'varie', 's')
text(ax, 44, 22, 'base : a = 6', 'autre', 's')
text(ax, 44, 15, r'hauteur : $10\times\sin 30°=5$', 'varie', 's')
text(ax, 44, 7, r'aire : $\frac{1}{2}\times 6\times 5=15$', 'resultat', 'm', weight='bold')
save(fig, '26-123')
