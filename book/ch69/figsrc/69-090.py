import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 85, r'en $x=0$', 'fixe', 'm')
xs = [8, 28, 48, 68]
vals = [r'$1$', r'$-3$', r'$-1$', r'$9/4$']
for x, v in zip(xs, vals):
    box(ax, x, 62, 14, 11, 'sujet', label=v)
for i in range(3):
    role = 'fixe' if i == 1 else 'varie'
    arrow(ax, (xs[i] + 7, 74), (xs[i + 1] + 7, 74), role, curve=-0.6)
text(ax, 44, 55, r'$V(0)=2$', 'resultat', 'l')
f = numberline(ax, 20, 68, 24, -2, 2, step=2, arrow_right=False)
V = {-2: 3, 0: 2, 2: 0}
pts = [(f(x), 24 + 4 * v) for x, v in V.items()]
line(ax, pts, 'fixe', dash=True)
for (x, v), (px, py) in zip(V.items(), pts):
    disc(ax, px, py, 1.6, 'resultat' if x == 0 else 'fixe')
    text(ax, px, py + 4.5, r'$V=%d$' % v, 'resultat' if x == 0 else 'fixe', 's')
save(fig, '69-090')
