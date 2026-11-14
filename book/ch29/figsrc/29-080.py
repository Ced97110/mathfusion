import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
cx, cy, R = 26, 31, 21
disc(ax, cx, cy, R, 'sujet')
poly(ax, [(cx, cy)] + arcp(cx, cy, R, 10, 80), 'varie')
line(ax, arcp(cx, cy, R, 10, 80), 'varie', lw=1.6)
text(ax, cx + 0.62 * R * math.cos(math.radians(45)), cy + 0.62 * R * math.sin(math.radians(45)), r'$\theta$', 'varie', 'l')
text(ax, cx, cy - R - 4, 'un tour = 2π ≈ 6,28', 'sujet', 'm')
text(ax, 70, 46, 'part du disque', 'encre', 's')
text(ax, 70, 33, r'$\frac{\theta}{2\pi}$', 'varie', 'xl')
arrow(ax, (43, 40), (59, 34), 'varie')
text(ax, cx - 8, cy - 8, 'disque', 'sujet', 's')
save(fig, '29-080')
