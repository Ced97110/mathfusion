import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Cardioïde r = 1 + cos θ : A (2 ; 0°) est sur la courbe ; son reflet gauche-droite (-2 ; 0) ne l'est pas : x >= -1/4
fig, ax = canvas(76)
o = (46, 40); u = 14
f = lambda t: 1 + math.cos(t)
# zone interdite : x < -1/4
xl = o[0] - 0.25 * u
ax.add_patch(Rectangle((2, 12), xl - 2, 56, fc=FILL['limite'], ec='none', zorder=0.5))
line(ax, [(xl, 12), (xl, 68)], 'limite', lw=1.0, dash=True)
text(ax, 18, 60, 'aucun point', 'limite', 's')
text(ax, 18, 55.5, 'de la courbe', 'limite', 's')
pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 300 for i in range(301)]]
line(ax, pts, 'sujet', lw=1.5)
arrow(ax, (3, o[1]), (o[0] + 2.6 * u, o[1]), 'fixe', lw=0.8)
text(ax, o[0] + 2.6 * u - 1, o[1] + 3.5, r'$x$', 'fixe', 's')
A = (o[0] + 2 * u, o[1]); Bm = (o[0] - 2 * u, o[1])
disc(ax, A[0], A[1], 1.5, 'sujet'); disc(ax, Bm[0], Bm[1], 1.6, 'limite', fill=False, lw=1.1); disc(ax, o[0], o[1], 0.8, 'encre')
arrow(ax, (A[0] - 2, A[1] + 7), (Bm[0] + 2, Bm[1] + 7), 'varie', lw=1.1, curve=0.35)
text(ax, A[0] + 4, A[1] + 4, 'A', 'sujet', 's')
text(ax, 60, 17, 'A : $r$ = 2 pour $\\theta$ = 0°', 'sujet', 's')
text(ax, Bm[0] + 3, Bm[1] - 5, '(−2 ; 0) : hors courbe', 'limite', 's')
text(ax, 55, 62, 'reflet gauche-droite', 'varie', 's')
text(ax, 44, 72, r'$r = 1 + \cos\theta$', 'sujet', 'm')
text(ax, 44, 7, r'$x = (u + \frac{1}{2})^2 - \frac{1}{4}$, avec $u = \cos\theta$ : $x \geq -\frac{1}{4}$', 'sujet', 's')
save(fig, '40-044')
