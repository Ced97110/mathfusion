import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, w = (1, 2, 3), (-3, 6, -3)
terms = [u[i] * w[i] for i in range(3)]
assert terms == [-3, 12, -9] and sum(terms) == 0
neg = lambda n: str(n).replace('-', '−')
fig, ax = canvas(58)
text(ax, 44, 53, r'$u=\langle 1,2,3\rangle$   $u\times v=\langle -3,6,-3\rangle$', 'encre', 's')
f = numberline(ax, 6, 78, 10, -4, 10, 1, every=2, arrow_right=False)
pos = 0
labs = [r'$1\times(-3)=-3$', r'$2\times6=12$', r'$3\times(-3)=-9$']
for i, t in enumerate(terms):
    y = 40 - i * 10
    a, b = f(pos), f(pos + t)
    arrow(ax, (a, y), (b, y), 'varie', lw=1.4)
    line(ax, [(a, y), (a, 10)], 'fixe', dash=True, lw=0.6)
    xm = (a + b) / 2
    text(ax, xm if i != 0 else xm + 14, y + 3.2, labs[i], 'varie', 's')
    pos += t
line(ax, [(f(pos), 40 - 2 * 10), (f(pos), 10)], 'resultat', dash=True, lw=0.9)
disc(ax, f(0), 10, 1.4, 'resultat')
text(ax, f(0) + 18, 15.5, r'$-3+12-9=0$', 'resultat', 's')
save(fig, '41-113')
