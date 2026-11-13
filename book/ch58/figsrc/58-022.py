import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# M1 : stocks (x, 0) ; M2 : stocks (0, y) ; la somme et le multiple restent dans M1
x0, y0, u = 12, 28, 7.6
P = lambda a, b: (x0 + a * u, y0 + b * u)
for a in range(0, 9):
    for b in range(0, 5):
        if b == 0 or a == 0:
            continue
        disc(ax, *P(a, b), 0.6, 'fixe')
for a in range(0, 9):
    disc(ax, *P(a, 0), 1.25, 'sujet')
for b in range(1, 5):
    disc(ax, *P(0, b), 1.25, 'autre')
line(ax, [P(0, 0), P(8.4, 0)], 'sujet', lw=0.6)
line(ax, [P(0, 0), P(0, 4.4)], 'autre', lw=0.6)
text(ax, P(8, 0)[0] - 3, P(8, 0)[1] + 4, r'$M_1$', 'sujet', 'm', weight='bold')
text(ax, P(0, 4)[0] + 4.5, P(0, 4)[1] + 3, r'$M_2$', 'autre', 'm', weight='bold')
# addition (2, 0) + (3, 0) = (5, 0) et multiplication 4 (2, 0) = (8, 0), sous l'axe
arrow(ax, (P(2, 0)[0], P(2, 0)[1] - 2.5), (P(5, 0)[0], P(5, 0)[1] - 2.5), 'varie', lw=1.3, curve=0.35)
arrow(ax, (P(2, 0)[0] - 1, P(2, 0)[1] - 2.5), (P(8, 0)[0], P(8, 0)[1] - 2.5), 'resultat', lw=1.3, curve=0.35)
text(ax, 22, 12, r'$(2,\ 0) + (3,\ 0) = (5,\ 0)$', 'varie', 's')
text(ax, 62, 12, r'$4\,(2,\ 0) = (8,\ 0)$', 'resultat', 's')
text(ax, 44, 4, 'le résultat reste dans M₁', 'fixe', 's')
save(fig, '58-022')
