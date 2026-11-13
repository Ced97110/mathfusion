import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(110)
import math
s = 0.48
ox, oy = 4 + 54.7 * s, 6 + 132.3 * s
T = lambda p: (ox + p[0] * s, oy + p[1] * s)
A, B, C = (0, 0), (60, 0), (37.5, math.sqrt(1093.75))
ex = [((75, 28.35), 28.35, 'a', '28,35'), ((-15, 39.69), 39.69, 'b', '39,69'), ((25, -66.14), 66.14, 'c', '66,14')]
for (c, r, k, v) in ex:
    disc(ax, *T(c), r * s, 'autre', fill=False, lw=0.9)
    line(ax, [T(c), T((c[0], 0))], 'varie', lw=1.3)
    disc(ax, *T(c), 0.7, 'autre')
poly(ax, [T(A), T(B), T(C)], 'sujet')
text(ax, T((75, 28.35))[0], T((75, 28.35))[1] + 5, 'touche le côté 40\n' + r'$r_a=\Delta\div 35\approx 28{,}35$', 'autre', 's')
text(ax, T((-15, 39.69))[0], T((-15, 39.69))[1] + 5, 'touche le côté 50\n' + r'$r_b=\Delta\div 25\approx 39{,}69$', 'autre', 's')
text(ax, T((25, -66.14))[0], T((25, -66.14))[1] - 6, 'touche le côté 60\n' + r'$r_c=\Delta\div 15\approx 66{,}14$', 'autre', 's')
text(ax, T((30, 0))[0] + 1, T((30, 0))[1] + 2.2, '60', 'sujet', 's')
text(ax, T((18, 18))[0] - 3, T((18, 18))[1] + 2, '50', 'sujet', 's')
text(ax, T((50, 18))[0] + 3, T((50, 18))[1] + 2.5, '40', 'sujet', 's')
save(fig, '37-115')
