import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(66)
R, th, O = 56, math.pi / 6, (12, 8)
P = (O[0] + R * math.cos(th), 8 + R * math.sin(th)); Hh = (P[0], 8)
line(ax, arc(O[0], O[1], R, 0, 1.0), 'fixe', dash=True)
poly(ax, [O, Hh, P], 'sujet')
line(ax, [O, P], 'sujet', lw=1.6); line(ax, [Hh, P], 'resultat', lw=2.4)
line(ax, [(Hh[0] - 3, 8), (Hh[0] - 3, 11), (Hh[0], 11)], 'fixe')
line(ax, arc(O[0], O[1], 14, 0, th), 'varie', lw=1.2)
text(ax, 36, 12.3, r'$\theta = 30°$', 'varie', 's')
text(ax, 8, 5.5, r'$O$'); text(ax, Hh[0], 4.5, r'$H$'); text(ax, P[0] + 3.5, P[1] + 2.5, r'$P$')
text(ax, 29, 31, 'OP = 1', 'sujet', 's'); text(ax, Hh[0] + 3, 22, 'HP = 0,5', 'resultat', 's', ha='left')
text(ax, 32, 47, r'$\sin\theta = HP / OP$', 'encre'); text(ax, 32, 40, r'$OP = 1$ donc $\sin\theta = HP$', 'resultat', 's')
save(fig, '29-108')
