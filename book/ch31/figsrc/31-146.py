import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(56)
text(ax, 44, 51, r'$(\sec\theta - 1)^2 = 0$', 'sujet', 'l')
f = numberline(ax, 12, 60, 12, 0, 3, 1, arrow_right=True)
k = 6.0
pts = [(f(0.0 + 3 * i / 40), 12 + k * (3 * i / 40 - 1) ** 2) for i in range(41)]
line(ax, pts, 'sujet', lw=1.2)
disc(ax, f(1), 12, 1.7, 'resultat')
text(ax, 78, 12, r'$\sec\theta$', 'sujet', 's')
text(ax, f(1), 4, '1', 'resultat', 's', weight='bold')
text(ax, f(1) + 3, 37, r'$\sec\theta = 1$', 'resultat', 's', ha='left')
arrow(ax, (f(1) + 2, 36), (f(1), 14.5), 'resultat')
text(ax, 70, 28, 'carré = 0', 'fixe', 's')
text(ax, 70, 24, 'une seule valeur', 'fixe', 's')
text(ax, f(1), 22, r'$\theta = 0°$', 'resultat', 's')
save(fig, '31-146')
