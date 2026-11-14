import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(66)
O = (6, 8); u = 28
X = O[0] + u
line(ax, [O, (X + 30, O[1])], 'fixe')
line(ax, [(X, O[1]), (X, O[1] + 1.732 * u)], 'fixe', dash=True)
rows = [(0.75, 'pente 0,75 : ≈ 36,87°', '≈ arrondi', 'varie'), (1, 'pente 1 : = 45°', '= exact', 'resultat'), (1.732, 'pente √3 : = 60°', '= exact', 'resultat')]
for m, lab, note, r in rows:
    line(ax, [O, (X, O[1] + m * u)], 'sujet', lw=1.3)
    text(ax, X + 2, O[1] + m * u + (0 if m != 0.75 else -1), lab, 'sujet', 's', ha='left')
    text(ax, 84, O[1] + m * u + (0 if m != 0.75 else -1), note, r, 's', ha='right')
text(ax, X, 3.5, 'avancée 1', 'fixe', 's')
save(fig, '25-115')
