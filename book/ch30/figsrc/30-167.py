import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, sx, sy = 14, 40, 64 / 7, 4
f = numberline(ax, x0, 78, y0, 0, 7, step=1, arrow_right=False, every=7)
line(ax, [(x0, 16), (x0, 64)], 'fixe')
line(ax, [(f(t / 20), y0 + 5 * sy * math.cos(2 * math.pi * (t / 20) / 7)) for t in range(0, 141)], 'sujet', lw=1.6)
xm, ym = f(3.5), y0 - 5 * sy
line(ax, [(xm, y0), (xm, ym)], 'fixe', dash=True)
line(ax, [(x0, ym), (xm, ym)], 'fixe', dash=True)
disc(ax, x0, y0 + 5 * sy, 1.4, 'fixe')
disc(ax, xm, ym, 1.6, 'resultat')
text(ax, 9, y0 + 5 * sy, '5', 'fixe', 's')
text(ax, 7, ym, '−5', 'resultat', 's')
text(ax, xm, 12, 'mi-période : 3,5 s', 'resultat', 's')
text(ax, 68, 17, r'$\cos\pi = -1$', 'sujet', 's')
text(ax, 46, 68, r'$d = 5\,\cos(2\pi t/7)$', 'sujet', 'm')
save(fig, '30-167')
