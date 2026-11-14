import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X = lambda x: 40 + x * 12
y0, sy = 36, 22
line(ax, [(14, y0), (84, y0)], 'fixe', lw=0.6)
def cv(a, b, role, lw, n=120):
    line(ax, [(X(a + (b - a) * i / n), y0 + sy * math.sin(a + (b - a) * i / n)) for i in range(n + 1)], role, lw=lw)
cv(-1.9, 3.5, 'fixe', 0.8); cv(-math.pi / 2, math.pi / 2, 'sujet', 2.2)
line(ax, [(14, y0 + sy * 0.5), (84, y0 + sy * 0.5)], 'varie', dash=True)
disc(ax, X(math.pi / 6), y0 + sy * 0.5, 1.5, 'resultat')
disc(ax, X(5 * math.pi / 6), y0 + sy * 0.5, 1.5, 'fixe', fill=False)
for v, s_, r in [(-math.pi / 2, r'$-\pi/2$', 'sujet'), (math.pi / 2, r'$\pi/2$', 'sujet'), (math.pi / 6, r'$\pi/6$', 'resultat'), (5 * math.pi / 6, r'$5\pi/6$', 'fixe')]:
    line(ax, [(X(v), y0 - 1), (X(v), y0 + 1)], r)
    text(ax, X(v), y0 - 4, s_, r, 's')
text(ax, 9, y0 + sy * 0.5, '0,5', 'varie', 's')
text(ax, 28, 71, r'sinus restreint à $[-\pi/2,\ \pi/2]$', 'sujet', 's')
text(ax, 62, 65, 'une seule solution : π/6', 'resultat', 's')
text(ax, 74, 56, 'hors intervalle', 'fixe', 's')
save(fig, '30-175')
