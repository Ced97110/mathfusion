import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def B(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(50)
u = 6; G = (5, 16); T = (G[0] + 4 * u, 16); H = (5, 16 + 3 * u)
poly(ax, [G, T, H], 'fixe'); rmark(ax, G, (1, 0), (0, 1), s=2)
line(ax, arcpts(T, 7, 143.13, 180), 'varie', lw=1.0)
text(ax, 2.5, 25, '3', 'encre', 'm'); text(ax, 17, 12.5, '4', 'encre', 'm'); text(ax, 19.5, 28, '5', 'encre', 'm')
text(ax, 18.6, 19.5, 'θ', 'varie', 's')
rows = [('sin', r'$\frac{3}{5}$', 'cosec', r'$\frac{5}{3}$'), ('cos', r'$\frac{4}{5}$', 'sec', r'$\frac{5}{4}$'), ('tan', r'$\frac{3}{4}$', 'cotan', r'$\frac{4}{3}$')]
for i, (a, fa, b, fb) in enumerate(rows):
    y = 28 - i * 13
    B(ax, 34, y, 24, 11, 'sujet', f'{a}  {fa}', 'm'); B(ax, 62, y, 24, 11, 'autre', f'{b}  {fb}', 'm')
text(ax, 60, 44.5, '3 × 2 = 6 quotients', 'resultat', 'm')
save(fig, '31-048')
