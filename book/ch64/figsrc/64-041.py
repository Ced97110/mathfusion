import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
xs = [6, 34, 62]; w = 20; h = 11
yt, yb = 56, 14
tops = [r'$\mathbb{Z}/6$', r'$\{0,2,4\}$', r'$\{0\}$']
bots = [r'$\mathbb{Z}/6$', r'$\{0,3\}$', r'$\{0\}$']
for i in range(3):
    box(ax, xs[i], yt, w, h, 'sujet', label=tops[i], size='m')
    box(ax, xs[i], yb, w, h, 'autre', label=bots[i], size='m')
gx = [30, 58]
for i in range(2):
    arrow(ax, (xs[i] + w + 0.3, yt + h / 2), (xs[i + 1] - 0.3, yt + h / 2), 'fixe')
    arrow(ax, (xs[i] + w + 0.3, yb + h / 2), (xs[i + 1] - 0.3, yb + h / 2), 'fixe')
rd = 2.8
ty, by = yt - 5.2, yb + h + 5.2
tf = [('2', 'varie', gx[0]), ('3', 'autre', gx[1])]
bf = {'3': gx[0], '2': gx[1]}
for lab, role, x in tf:
    x2 = bf[lab]
    d = math.hypot(x2 - x, by - ty)
    ux, uy = (x2 - x) / d, (by - ty) / d
    line(ax, [(x + ux * rd, ty + uy * rd), (x2 - ux * rd, by - uy * rd)], role, lw=1.0)
    disc(ax, x, ty, rd, role, label=lab, size='m')
    disc(ax, x2, by, rd, role, label=lab, size='m')
text(ax, 44, 5, 'facteurs appariés : 2↔2, 3↔3', 'encre', 's')
save(fig, '64-041')
