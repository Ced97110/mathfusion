import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(58)
R, th, O = 50, 0.6, (10, 8)
A = (O[0] + R, 8); P = (O[0] + R * math.cos(th), 8 + R * math.sin(th)); Hh = (P[0], 8); T = (A[0], 8 + R * math.tan(th))
line(ax, arc(O[0], O[1], R, 0, 1.2), 'fixe', dash=True)
line(ax, [O, A], 'fixe'); line(ax, [O, T], 'fixe')
line(ax, arc(O[0], O[1], R, 0, th), 'varie', lw=2.4)
line(ax, [Hh, P], 'encre', lw=2.4); line(ax, [A, T], 'resultat', lw=2.4)
for p in (P, A, T, Hh): disc(ax, p[0], p[1], 0.8, 'encre')
text(ax, 6, 5, r'$O$'); text(ax, A[0], 4.5, r'$A$'); text(ax, Hh[0], 4.5, r'$H$')
text(ax, P[0] - 4, P[1] + 3.5, r'$P$'); text(ax, T[0] + 3, T[1] + 2.5, r'$T$')
text(ax, 35, 4.5, 'rayon 1', 'fixe', 's')
text(ax, 47, 19, r'$\sin\theta$', 'encre', 's'); text(ax, 55.8, 18, r'$\theta$', 'varie', 's'); text(ax, 74, 26, r'$\tan\theta$', 'resultat', 'm')
save(fig, '29-107')
