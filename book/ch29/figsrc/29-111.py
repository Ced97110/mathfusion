import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(58)
R, th, O = 46, 0.6, (10, 8)
A = (O[0] + R, 8); T = (A[0], 8 + R * math.tan(th))
line(ax, [O, A], 'sujet', lw=1.8); line(ax, [O, T], 'fixe'); line(ax, [A, T], 'resultat', lw=2.4)
for k in range(8):
    y = 8 + 4.6 * k; l_ = 4 if k == 5 else 2.5
    line(ax, [(A[0], y), (A[0] + l_, y)], 'encre', lw=0.7)
text(ax, A[0] + 7, 8, '0', 'encre', 's'); text(ax, A[0] + 8, 31, '0,5', 'encre', 's')
disc(ax, T[0], T[1], 0.9, 'resultat'); text(ax, T[0] - 3, T[1] + 2.5, r'$T$')
line(ax, arc(O[0], O[1], 12, 0, th), 'varie', lw=1.2); text(ax, 31, 11.5, r'$\theta = 0{,}6$', 'varie', 's')
text(ax, 6, 5.5, r'$O$'); text(ax, A[0], 4.5, r'$A$'); text(ax, 33, 4.5, 'OA = 1', 'sujet', 's')
text(ax, 75, 20, r'$AT \approx 0{,}684$', 'resultat', 's')
text(ax, 34, 50, r'$\tan\theta = AT / OA = AT / 1$', 'resultat')
save(fig, '29-111')
