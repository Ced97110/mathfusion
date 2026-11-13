import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Règle de lecture : seulement cos θ -> symétrie par l'axe x ; seulement sin θ -> symétrie par l'axe y
fig, ax = canvas(84)
u = 5.5
def curve(o, f, role):
    pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 360 for i in range(361)]]
    line(ax, pts, role, lw=1.4)
oa = (17, 42); ob = (65, 34)
curve(oa, lambda t: 3 + 2 * math.cos(t), 'sujet')
curve(ob, lambda t: 3 + 2 * math.sin(t), 'autre')
# axes de symétrie
line(ax, [(oa[0] - 10, oa[1]), (oa[0] + 36, oa[1])], 'varie', lw=1.0, dash=True)
line(ax, [(ob[0], ob[1] - 12), (ob[0], ob[1] + 36)], 'varie', lw=1.0, dash=True)
disc(ax, oa[0], oa[1], 0.8, 'encre'); disc(ax, ob[0], ob[1], 0.8, 'encre')
text(ax, 30, 77, r'seulement $\cos\theta$', 'sujet', 'm')
text(ax, 66, 77, r'seulement $\sin\theta$', 'autre', 'm')
text(ax, 30, 71, r'$r = 3 + 2\cos\theta$', 'sujet', 's')
text(ax, 66, 71, r'$r = 3 + 2\sin\theta$', 'autre', 's')
text(ax, 34, 16, 'symétrique par', 'varie', 's')
text(ax, 34, 12, 'l’axe des $x$', 'varie', 's')
text(ax, 68, 16, 'symétrique par', 'varie', 's')
text(ax, 68, 12, 'l’axe des $y$', 'varie', 's')
text(ax, 34, 6, r'$\cos(-\theta) = \cos\theta$', 'sujet', 's')
text(ax, 68, 6, r'$\sin(\pi-\theta) = \sin\theta$', 'autre', 's')
save(fig, '40-045')
