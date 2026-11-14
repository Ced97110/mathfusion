import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs, ys, x0, y0, ymax = 20.0, 3.8, 44.0, 16.0, 12.0
def curve(f, role, lw=1.4):
    pts = []
    n = 80
    for i in range(n + 1):
        x = -1.7 + 3.4 * i / n
        v = f(x)
        if v <= ymax: pts.append((x0 + x * xs, y0 + v * ys))
    line(ax, pts, role, lw=lw)
line(ax, [(x0 - 1.8 * xs, y0), (x0 + 1.8 * xs, y0)], 'fixe', lw=1.8)
text(ax, 3, y0 - 5, 'axe : valeur 0\naucune courbe ne le touche', 'fixe', 's', ha='left')
curve(lambda x: x ** 4 + 4, 'sujet', 1.6)
curve(lambda x: x * x - 2 * x + 2, 'varie')
curve(lambda x: x * x + 2 * x + 2, 'autre')
# x = 1 : g = 1, h = 5, f = 5
line(ax, [(x0 + xs, y0 - 1), (x0 + xs, y0 + 6 * ys)], 'fixe', dash=True, lw=0.7)
for v, role in ((1, 'varie'), (5, 'autre'), (5, 'sujet')):
    disc(ax, x0 + xs, y0 + v * ys, 0.9 if role != 'sujet' else 1.4, role, fill=(role != 'sujet'))
text(ax, 20, 75, r'$f=x^4+4$', 'sujet', 'm')
text(ax, 50, 75, r'$g=x^2-2x+2$', 'varie', 'm')
text(ax, 70, 69, r'$h=x^2+2x+2$', 'autre', 'm')
text(ax, x0 + xs + 1.5, y0 - 4, 'x = 1', 'encre', 's')
text(ax, x0 + xs + 2, y0 + 1 * ys + 4.5, '$g=1$', 'varie', 's', ha='left')
text(ax, x0 + xs - 3, y0 + 5 * ys + 8, '$h=5$ et $f=5$', 'autre', 's', ha='right')
text(ax, 44, 5, r'en $x=1$ : $g\times h=1\times5=5=f$', 'encre', 'm')
save(fig, '54-211')
