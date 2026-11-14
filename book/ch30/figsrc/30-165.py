import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
x0, y0, sx, sy = 14, 40, 64 / 7, 4
f = numberline(ax, x0, 78, y0, 0, 7, step=1, arrow_right=False, every=7)
line(ax, [(x0, 18), (x0, 62)], 'fixe')
pts = [(f(t / 20), y0 + 5 * sy * math.cos(2 * math.pi * (t / 20) / 7)) for t in range(0, 141)]
line(ax, pts, 'sujet', lw=1.6)
disc(ax, x0, y0 + 5 * sy, 1.4, 'resultat')
text(ax, 9, y0 + 5 * sy, '5', 'fixe', 's')
text(ax, 8, y0 - 5 * sy, '−5', 'fixe', 's')
text(ax, 14, 66, 'd (cm)', 'fixe', 's')
text(ax, 84, y0, 't (s)', 'fixe', 's')
text(ax, 46, 71, r'$d = 5\,\cos(2\pi t/7)$', 'sujet', 'm')
brace(ax, x0, 78, 15, 'varie', label='période 7 s')
save(fig, '30-165')
