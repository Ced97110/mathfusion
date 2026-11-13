import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(66)
s = 14
O = (14, 16); N = (O[0] + 3 * math.cos(1) * s, 16); P = (N[0], 16 + 3 * math.sin(1) * s)
poly(ax, [O, N, P], 'sujet')
line(ax, [O, N], 'resultat', lw=2.2)
line(ax, [(N[0] - 3, N[1]), (N[0] - 3, N[1] + 3), (N[0], N[1] + 3)], 'fixe')
line(ax, arc(O[0], O[1], 7, 0, 1), 'varie', lw=1.2)
text(ax, 28, 21, '1 rad', 'varie', 's')
text(ax, 11, 13, r'$O$'); text(ax, N[0] + 1, 12.5, r'$N$'); text(ax, P[0], P[1] + 3.5, r'$P$')
text(ax, 17, 40, 'OP = 3 cm', 'sujet', 's')
text(ax, 25, 12.5, r'$ON$', 'resultat', 's')
text(ax, 66, 34, r'$\cos 1 \approx 0{,}5403$', 'encre', 's')
text(ax, 44, 5, r'$ON = 3\cos 1 \approx 1{,}6209$ cm', 'resultat', 'm')
save(fig, '29-098')
