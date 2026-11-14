import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(68)
cx, cy, r = 24, 36, 20
disc(ax, cx, cy, r, 'fixe', fill=False)
v = [P(cx, cy, r, 72 * i) for i in range(5)]
poly(ax, v, 'sujet')
line(ax, [(2, cy), (46, cy)], 'fixe')
line(ax, [(cx, cy), v[1]], 'sujet')
c = (cx + r * math.cos(math.radians(72)), cy)
line(ax, [v[1], c], 'varie', dash=True)
for p in v: disc(ax, p[0], p[1], 1.2, 'sujet')
disc(ax, c[0], c[1], 1.4, 'varie')
text(ax, v[1][0] + 1, v[1][1] + 3.8, r'$\zeta$', 'sujet')
text(ax, c[0] + 1, cy - 4, r'$c$', 'varie')
a = [P(cx, cy, 7, 3 * i) for i in range(0, 25)]
line(ax, a, 'varie')
text(ax, 24 + 12 * math.cos(math.radians(30)) + 3, cy + 12 * math.sin(math.radians(30)) + 1, '72°', 'varie', 's')
X, W = 52, 34
box(ax, X, 50, W, 12, 'sujet', label='construire\nle 5-gone', size='s')
box(ax, X, 30, W, 12, 'varie', label='construire\n' + r'$\cos(2\pi/5)\approx0{,}309$', size='s')
box(ax, X, 10, W, 12, 'resultat', label='son degré : 2\n' + r'(avec $\varphi(5)=4$)', size='s')
arrow(ax, (X + W / 2, 50), (X + W / 2, 42.5), 'varie'); arrow(ax, (X + W / 2, 30), (X + W / 2, 22.5), 'varie')
save(fig, '66-011')
