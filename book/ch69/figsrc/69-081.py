import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
Y0 = 24
f = numberline(ax, 14, 72, Y0, -2, 2, step=1)
g = lambda x: x ** 3 - 3 * x + 1
n = 80
pts = [(f(-2 + 4 * i / n), Y0 + 8 * g(-2 + 4 * i / n)) for i in range(n + 1)]
line(ax, pts, 'sujet', lw=1.3)
for r, lab, dx in [(-1.879, r'$r_1$', -4.5), (0.347, r'$r_2$', 4.5), (1.532, r'$r_3$', -4.5)]:
    disc(ax, f(r), Y0, 1.3, 'resultat')
    text(ax, f(r) + dx, Y0 + 5, lab, 'resultat', 's')
for v in (-2, 2):
    box(ax, f(v) - 2, Y0 + 8 * g(v) - 2, 4, 4, 'varie')
text(ax, f(-2) + 4, Y0 - 8, r'$f(a)=-1\neq 0$', 'varie', 's', ha='left')
text(ax, f(2) - 4, Y0 + 24, r'$f(b)=3\neq 0$', 'varie', 's', ha='right')
text(ax, 44, 5, 'bornes a = −2 et b = 2 : pas des racines', 'encre', 's')
save(fig, '69-081')
