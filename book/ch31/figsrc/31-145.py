import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(52)
text(ax, 44, 46, r'$c^2 = c + 1$ avec $c = \cos\theta$', 'sujet', 'm')
f = numberline(ax, 8, 62, 22, -1, 2, 1, arrow_right=True)
ax.add_patch(Rectangle((f(-1), 19.5), f(1) - f(-1), 5, fc=FILL['resultat'], ec=COL['resultat'], lw=0.8, zorder=1))
text(ax, (f(-1) + f(1)) / 2, 30, r'$\cos\theta$ possible', 'resultat', 's')
disc(ax, f(-0.618), 22, 1.6, 'resultat'); disc(ax, f(1.618), 22, 1.6, 'limite')
text(ax, f(-0.618), 12, '−0,618', 'resultat', 's'); text(ax, f(1.618), 12, '1,618', 'limite', 's')
text(ax, f(1.618), 36, 'impossible', 'limite', 's')
arrow(ax, (f(1.618), 34), (f(1.618), 25), 'limite')
text(ax, 44, 5, r'$\theta \approx 128{,}17°$ ou $231{,}83°$', 'resultat', 's')
save(fig, '31-145')
