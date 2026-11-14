import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0 = 14; y0 = 14; su = 28; hu = 0.7
f = numberline(ax, x0, x0 + 2 * su, y0, 0, 2, step=0.5, arrow_right=False, every=1)
line(ax, [(x0, y0), (x0, y0 + 64 * hu + 3)], 'fixe')
text(ax, x0, y0 + 64 * hu + 7, 'h (pieds)', 'fixe', 's', ha='left')
text(ax, x0 + 2 * su + 9, y0, 't (s)', 'fixe', 's')
n = 40
line(ax, [(f(2 * i / n), y0 + (64 - 16 * (2 * i / n) ** 2) * hu) for i in range(n + 1)], 'sujet', lw=1.4)
for t, h in [(0, 64), (1, 48), (1.5, 28), (2, 0)]:
    yp = y0 + h * hu
    if 0 < t < 2: line(ax, [(x0, yp), (f(t), yp)], 'fixe', lw=0.6, dash=True)
    disc(ax, f(t), yp, 1.2, 'varie' if h else 'resultat')
    if t < 2: text(ax, x0 - 4, yp, str(h), 'varie', 's')
text(ax, f(2) - 2, y0 + 5, 'au sol : 0', 'resultat', 's', ha='right')
text(ax, 62, 56, r'$h=64-16t^2$', 'encre', 'm')
save(fig, '23-005')
