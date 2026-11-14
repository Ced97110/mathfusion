import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(48)
f = numberline(ax, 6, 80, 12, 20, 50, step=10, arrow_right=False)
for v, r, val, hi in [(26.565, '0,5', '26,565', False), (36.870, '0,75', '36,870', True), (41.987, '0,9', '41,987', False)]:
    x = f(v); ytop = 36 if hi else 24
    disc(ax, x, 12, 1.3, 'resultat')
    line(ax, [(x, 13.5), (x, ytop - 2.5)], 'resultat', lw=0.7, dash=True)
    text(ax, x, ytop + 2.2, r'$\arctan\ ' + r.replace(',', '{,}') + '$', 'encre', 's')
    text(ax, x, ytop - 1.0, '≈ ' + val + '°', 'resultat', 's')
text(ax, 44, 2.5, 'angle en degrés (arrondi à 3 décimales)', 'fixe', 's')
save(fig, '25-079')
