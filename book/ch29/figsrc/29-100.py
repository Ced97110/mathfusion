import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(56)
O = (12, 30); r = 26; P = (O[0] + r, O[1])
line(ax, arc(O[0], O[1], r, -0.7, 0.7), 'fixe', dash=True)
line(ax, [O, P], 'sujet', lw=2.2)
disc(ax, P[0], P[1], 1.3, 'varie')
text(ax, 7.5, 30, r'$O$'); text(ax, 25, 33.5, r'$r$', 'sujet')
text(ax, 41, 30, r'$P = Q$', 'varie', 'm', ha='left')
text(ax, 14, 39, r'$\theta = 0$', 'varie')
text(ax, 71, 46, 'arc', 'encre'); text(ax, 71, 40, r'$s = r \times 0 = 0$', 'resultat')
text(ax, 71, 28, 'aire', 'encre'); text(ax, 71, 21, r'$A = \frac{1}{2}r^2 \times 0 = 0$', 'resultat')
text(ax, 44, 6, 'le secteur est un simple trait', 'encre')
save(fig, '29-100')
