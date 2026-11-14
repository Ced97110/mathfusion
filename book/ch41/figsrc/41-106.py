import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

nu, nv = 2.0, 5 ** 0.5
sn = 2 / nv
assert abs(nu * nv * sn - 4) < 1e-9
fig, ax = canvas(54)
text(ax, 44, 49, r'$\|u\times v\|=\|u\|\,\|v\|\sin\theta$', 'encre', 'l')
w, g = 17.5, 4.5
x0 = (88 - 4 * w - 3 * g) / 2
labs = [(r'$\|u\|=2$', 'sujet'), (r'$\|v\|\approx2{,}236$', 'autre'), (r'$\sin\theta\approx0{,}894$', 'varie'), ('= 4', 'resultat')]
for i, (lab, role) in enumerate(labs):
    x = x0 + i * (w + g)
    box(ax, x, 34, w, 8, role, label=lab, size='s')
    if i < 3:
        text(ax, x + w + g / 2, 38, '×' if i < 2 else '=', 'encre', 's')
o = (12, 8); s = 9
P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
poly(ax, [P((0, 0)), P((2, 0)), P((3, 2)), P((1, 2))], 'sujet')
arrow(ax, P((0, 0)), P((2, 0)), 'sujet', lw=1.2)
arrow(ax, P((0, 0)), P((1, 2)), 'autre', lw=1.2)
line(ax, [P((1, 2)), P((1, 0))], 'varie', dash=True, lw=1.2)
text(ax, P((1, 0))[0] + 8, P((1, 0))[1] - 3.2, r'base 2', 'sujet', 's')
text(ax, P((0.5, 1))[0] - 3, P((0.5, 1))[1] + 1, r'$v$', 'autre')
text(ax, P((1, 1))[0] + 1.2, P((1, 1))[1] - 3, 'hauteur 2', 'varie', 's', ha='left')
text(ax, P((0, 0))[0] + 7, P((0, 0))[1] + 3, r'$\theta$', 'encre', 's')
text(ax, 64, 26, 'aire = 2 × 2 = 4', 'resultat', 's')
save(fig, '41-106')
