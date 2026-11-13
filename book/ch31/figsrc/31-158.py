import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(56)
u = 13.0; O = (24, 6)
for k in range(-1, 3):
    line(ax, [(O[0] + k * u, O[1] - 1.5 * 0), (O[0] + k * u, O[1] + 2.6 * u)], 'fixe', 0.3)
for k in range(0, 3):
    line(ax, [(O[0] - 1.4 * u, O[1] + k * u), (O[0] + 2.6 * u, O[1] + k * u)], 'fixe', 0.3)
arrow(ax, (O[0] - 1.5 * u, O[1]), (O[0] + 2.8 * u, O[1]), 'fixe', 0.9); arrow(ax, (O[0], O[1] - 3), (O[0], O[1] + 2.9 * u), 'fixe', 0.9)
P = (O[0] + 2 * u, O[1] + u); Q = (O[0] - u, O[1] + 2 * u)
line(ax, [O, P], 'sujet', 1.0); line(ax, [O, Q], 'resultat', 1.0)
disc(ax, *P, 1.5, 'sujet'); disc(ax, *Q, 1.5, 'resultat')
arc(ax, O, 12, math.degrees(math.atan2(1, 2)) + 3, 90 + math.degrees(math.atan2(1, 2)) - 3 + 0, 'varie', 1.2)
arrow(ax, (O[0] + 12 * math.cos(math.radians(100)), O[1] + 12 * math.sin(math.radians(100))), (O[0] + 12 * math.cos(math.radians(112)), O[1] + 12 * math.sin(math.radians(112))), 'varie', 1.2)
text(ax, P[0] + 2, P[1] - 3.5, '(2 ; 1)', 'sujet', 's', ha='left')
text(ax, Q[0] - 1, Q[1] + 4, '(−1 ; 2)', 'resultat', 's')
text(ax, O[0] + 12, O[1] + 20, '90°', 'varie', 's')
text(ax, 72, 46, r'$\cos 90° = 0$, $\sin 90° = 1$', 'fixe', 's') if False else None
text(ax, 71, 46, 'cos 90° = 0', 'fixe', 's'); text(ax, 71, 41, 'sin 90° = 1', 'fixe', 's')
text(ax, 71, 32, 'x′ = 2×0 − 1×1', 'varie', 's'); text(ax, 71, 27, '= −1', 'resultat', 's')
text(ax, 71, 18, 'y′ = 2×1 + 1×0', 'varie', 's'); text(ax, 71, 13, '= 2', 'resultat', 's')
save(fig, '31-158')
