import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(62)
R = 26.0; O = (26, 31)
V = [(O[0] + R * math.cos(math.radians(72 * k)), O[1] + R * math.sin(math.radians(72 * k))) for k in range(5)]
poly(ax, V, 'sujet')
line(ax, [O, V[0]], 'fixe', 1.0); line(ax, [O, V[1]], 'fixe', 1.0)
H_ = (V[1][0], O[1])
line(ax, [V[1], H_], 'fixe', 0.8, dash=True)
line(ax, [O, H_], 'resultat', 2.0)
arc(ax, O, 8, 0, 72, 'varie', 1.1)
text(ax, O[0] + 12, O[1] + 6.5, r'$72°$', 'varie', 's')
text(ax, O[0] + 4, O[1] - 3, '0,3090', 'resultat', 's')
text(ax, O[0] + 20, O[1] - 3, '1', 'fixe', 's') if False else text(ax, 56 - 1, O[1] + 12, '', 'fixe', 's') if False else None
text(ax, 44, 8, '5 côtés égaux', 'sujet', 's') if False else None
text(ax, 72, 52, r'$\cos 72° \approx 0{,}3090$', 'resultat', 's')
text(ax, 72, 40, '0,3090 = 0,618 ÷ 2', 'fixe', 's')
text(ax, 72, 32, '0,618 = 1 ÷ 1,618', 'fixe', 's')
text(ax, 72, 20, 'pentagone régulier', 'sujet', 's')
text(ax, 72, 15, 'règle et compas', 'sujet', 's')
text(ax, 72, 10, 'constructible', 'sujet', 's')
save(fig, '31-154')
