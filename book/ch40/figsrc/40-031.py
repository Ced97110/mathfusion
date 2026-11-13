import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# r négatif : θ = 60°, r = cos 3θ = -1 : x = -1 × 0,5 = -0,5 ; y = -1 × 0,866 ≈ -0,866
fig, ax = canvas(88)
o = (40, 44); u = 24
c, s = math.cos(math.radians(60)), math.sin(math.radians(60))
line(ax, [(o[0] - 30, o[1]), (o[0] + 32, o[1])], 'fixe')
line(ax, [(o[0], o[1] - 31), (o[0], o[1] + 31)], 'fixe')
text(ax, o[0] + 34, o[1] - 3, r'$x$', 'fixe', 's')
text(ax, o[0] + 3, o[1] + 33, r'$y$', 'fixe', 's')
line(ax, [(o[0] - 1.3 * u * c, o[1] - 1.3 * u * s), (o[0] + 1.3 * u * c, o[1] + 1.3 * u * s)], 'fixe', dash=True)
g = (o[0] + u * c, o[1] + u * s)          # point si r = +1
q = (o[0] - u * c, o[1] - u * s)          # point pour r = -1
disc(ax, g[0], g[1], 1.3, 'fixe', fill=False)
disc(ax, q[0], q[1], 1.5, 'sujet')
disc(ax, o[0], o[1], 0.9, 'encre')
arrow(ax, (o[0] - 0.5, o[1] - 0.8), (q[0] + 0.7, q[1] + 1.2), 'varie', lw=1.4)
# arc de l'angle 60°
pts = [(o[0] + 8 * math.cos(math.radians(a)), o[1] + 8 * math.sin(math.radians(a))) for a in range(0, 61, 3)]
line(ax, pts, 'varie', lw=1.1)
text(ax, o[0] + 14, o[1] + 4, r'$\theta$ = 60°', 'varie', 's')
text(ax, g[0] + 9, g[1] + 3, r'si $r$ = 1', 'fixe', 's')
text(ax, q[0] + 17, q[1] - 4, r'$r$ = $-1$', 'sujet', 'm')
text(ax, o[0] - 3, o[1] + 3, 'O', 'encre', 's')
text(ax, 44, 9, r'$x = -1 \times 0{,}5 = -0{,}5$', 'sujet', 's')
text(ax, 44, 4, r'$y = -1 \times 0{,}866 \approx -0{,}866$', 'sujet', 's')
text(ax, 44, 85, r'$-r$ : de l’autre côté de O', 'varie', 'm')
save(fig, '40-031')
