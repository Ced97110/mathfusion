import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=300, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t1 * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(72)
x0, w, y0, k = 8, 70, 44, 4.4
arrow(ax, (x0, y0), (x0 + w + 6, y0), 'fixe', 0.8)
wave(ax, lambda t: 3 * math.sin(t), x0, w, y0, k, 'sujet', 1.3)
wave(ax, lambda t: 4 * math.cos(t), x0, w, y0, k, 'varie', 1.3)
line(ax, [(x0, y0 + 4 * k), (x0 + w, y0 + 4 * k)], 'varie', 0.6, True)
line(ax, [(x0 + w / 4, y0 + 3 * k), (x0 + w, y0 + 3 * k)], 'sujet', 0.6, True)
text(ax, 84, y0 + 3 * k, '3', 'sujet', 's'); text(ax, 84, y0 + 4 * k, '4', 'varie', 's')
text(ax, 61, y0 - 3 * k - 3.5, r'$3\,\sin x$', 'sujet', 's')
text(ax, 22, y0 + 4 * k + 3, r'$4\,\cos x$', 'varie', 's')
for xx in (x0, x0 + w / 4): line(ax, [(xx, y0), (xx, y0 - 6)], 'fixe', 0.6, True)
arrow(ax, (x0, y0 - 5), (x0 + w / 4, y0 - 5), 'varie', 1.0)
text(ax, 17, y0 - 11, 'un quart de période', 'varie', 's')
text(ax, 12, 14, r'$y\;=$', 'encre', 'l'); text(ax, 29, 14, r'$3\,\sin x$', 'sujet', 'l')
text(ax, 41, 14, '+', 'encre', 'l'); text(ax, 56, 14, r'$4\,\cos x$', 'varie', 'l')
save(fig, '35-001')
