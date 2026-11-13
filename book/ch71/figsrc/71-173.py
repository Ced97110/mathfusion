import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = (44, 38); us, ut = 40, 28
ts = [i / 200 * 2 * math.pi for i in range(201)]
arrow(ax, (c[0] - 38, c[1]), (c[0] + 38, c[1]), 'fixe', lw=0.7)
arrow(ax, (c[0], c[1] - 33), (c[0], c[1] + 33), 'fixe', lw=0.7)
line(ax, [(c[0] + 0.5 * us * math.cos(t), c[1] + ut * math.sin(t)) for t in ts], 'sujet', lw=1.2)
for sx, sy in [(0.5, 0), (-0.5, 0), (0, 1), (0, -1)]:
    disc(ax, c[0] + sx * us, c[1] + sy * ut, 1.5, 'resultat')
text(ax, c[0] + 20 + 4, c[1] - 4, r'$\frac{1}{2}$', 'resultat', 's')
text(ax, c[0] - 20 - 4, c[1] - 4, r'$-\frac{1}{2}$', 'resultat', 's')
text(ax, c[0] + 6, c[1] + ut + 1, '1', 'resultat', 's')
text(ax, c[0] + 6, c[1] - ut - 1, '−1', 'resultat', 's')
text(ax, c[0] + 38, c[1] + 4, '$s$', 'fixe', 's'); text(ax, c[0] + 4, c[1] + 33, '$t$', 'fixe', 's')
text(ax, 6, 76, r'$4s^2 + t^2 = 1$', 'sujet', 'm', ha='left')
save(fig, '71-173')
